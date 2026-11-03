"""Build every processed table used by the notebooks, from the raw CSV.

Cleaning rules, applied in this order and stated in every notebook:
1. Drop rows where the invoice number starts with C. Those are cancellations.
2. Drop rows with quantity at or below zero, or unit price at or below zero.
3. Drop rows with no CustomerID. RFM needs a customer, and 135,080 raw
   rows have no CustomerID. Those rows are counted, not hidden.
4. Revenue for a line = Quantity x UnitPrice, in pounds sterling.

Reference date for recency: one day after the last clean transaction,
10 December 2011. December 2011 is a partial month (data stop on
9 December 2011), so it is excluded from complete month averages and
from the forecast training set, and it is flagged wherever it appears.

Original metric, Recency Gap Ratio, defined in notebook 05:
  gap ratio = days since last order / median gap between that
  customer's own past orders.
A ratio above 2 means the customer has waited more than twice as
long as usual. It is a warning signal, not a proven churn prediction.

Simple customer value estimate, also in notebook 05:
  CLV estimate (2 years) = average order value x orders per year x 2.
Orders per year uses time from first order to the reference date.
It assumes the past rate continues, which it may not. Report the
median, not the mean, because a few wholesale buyers distort the mean.

Run from the project root:
    python scripts/build_processed.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "online_retail.csv"
OUT = ROOT / "data" / "processed"
OUT.mkdir(parents=True, exist_ok=True)


def clean(df):
    raw_rows = len(df)
    df = df.copy()
    cancelled = df["InvoiceNo"].astype(str).str.startswith("C").sum()
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
    missing_customer = int(df["CustomerID"].isna().sum())
    df = df.dropna(subset=["CustomerID"])
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    print(f"Raw rows: {raw_rows}, cancelled rows: {cancelled}, "
          f"missing CustomerID before drop: {missing_customer}, clean rows: {len(df)}")
    return df


def rfm_table(df, ref):
    rfm = df.groupby("CustomerID").agg(
        recency=("InvoiceDate", lambda x: (ref - x.max()).days),
        frequency=("InvoiceNo", "nunique"),
        monetary=("Revenue", "sum"),
    ).reset_index()

    def score(series, reverse=False):
        ranks = pd.qcut(series, 4, labels=False, duplicates="drop")
        return (3 - ranks if reverse else ranks) + 1

    rfm["R_score"] = score(rfm["recency"], reverse=True)
    rfm["F_score"] = score(rfm["frequency"])
    rfm["M_score"] = score(rfm["monetary"])
    rfm["RFM_total"] = rfm["R_score"] + rfm["F_score"] + rfm["M_score"]

    def segment(row):
        if row["RFM_total"] >= 10:
            return "Champions"
        if row["RFM_total"] >= 8:
            return "Loyal"
        if row["R_score"] >= 3 and row["F_score"] >= 2:
            return "Potential loyal"
        if row["R_score"] >= 3:
            return "Recent buyers"
        if row["R_score"] == 2 and row["F_score"] >= 2:
            return "At risk"
        return "Lost or hibernating"

    rfm["segment"] = rfm.apply(segment, axis=1)
    return rfm


def gap_and_clv(df, ref):
    order_rev = df.groupby(["CustomerID", "InvoiceNo"]).agg(
        order_revenue=("Revenue", "sum"), order_date=("InvoiceDate", "min")
    ).reset_index()
    rows = []
    for customer, sub in order_rev.sort_values("order_date").groupby("CustomerID"):
        dates = sub["order_date"].sort_values()
        gaps = dates.diff().dt.days.dropna()
        median_gap = gaps.median() if len(gaps) >= 1 else float("nan")
        days_since = (ref - dates.max()).days
        gap_ratio = days_since / median_gap if median_gap and median_gap > 0 else float("nan")
        rows.append({
            "CustomerID": customer,
            "orders": len(sub),
            "first_order": dates.min(),
            "last_order": dates.max(),
            "median_gap_days": median_gap,
            "days_since_last": days_since,
            "gap_ratio": gap_ratio,
            "average_order_value": sub["order_revenue"].mean(),
            "total_spent": sub["order_revenue"].sum(),
        })
    table = pd.DataFrame(rows)
    table["years_seen"] = (ref - table["first_order"]).dt.days / 365.25
    table["orders_per_year"] = table["orders"] / table["years_seen"]
    table["clv_2yr_estimate"] = table["average_order_value"] * table["orders_per_year"] * 2
    return table


def main():
    df = pd.read_csv(RAW, encoding="utf-8")
    df = clean(df)
    df.to_csv(OUT / "clean_transactions.csv", index=False)

    monthly = df.groupby(df["InvoiceDate"].dt.to_period("M")).agg(
        revenue=("Revenue", "sum"), orders=("InvoiceNo", "nunique"),
        lines=("Revenue", "size"), customers=("CustomerID", "nunique"),
    ).reset_index()
    monthly["month"] = monthly["InvoiceDate"].astype(str)
    monthly = monthly.drop(columns=["InvoiceDate"])
    monthly.to_csv(OUT / "monthly_sales.csv", index=False)

    ref = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    rfm = rfm_table(df, ref)
    rfm.to_csv(OUT / "rfm_segments.csv", index=False)

    gap = gap_and_clv(df, ref)
    gap.to_csv(OUT / "customer_gap_clv.csv", index=False)

    country = df.groupby("Country").agg(
        revenue=("Revenue", "sum"), orders=("InvoiceNo", "nunique"),
        customers=("CustomerID", "nunique")).reset_index().sort_values("revenue", ascending=False)
    country.to_csv(OUT / "country_sales.csv", index=False)

    product = df.groupby(["StockCode", "Description"]).agg(
        revenue=("Revenue", "sum"), quantity=("Quantity", "sum"),
        lines=("Revenue", "size")).reset_index().sort_values("revenue", ascending=False)
    product.to_csv(OUT / "product_sales.csv", index=False)

    # Forecast backtest: 3 month moving average, complete months only.
    complete = monthly[monthly["month"] != "2011-12"].copy()
    complete["forecast_3m_avg"] = complete["revenue"].shift(1).rolling(3).mean()
    complete["abs_pct_error"] = (complete["forecast_3m_avg"] - complete["revenue"]).abs() / complete["revenue"] * 100
    complete.to_csv(OUT / "forecast_backtest.csv", index=False)
    print("Reference date:", ref.date())
    print("Clean revenue, pounds:", round(df["Revenue"].sum(), 2))
    print("Customers:", df["CustomerID"].nunique())
    print("Wrote processed tables to", OUT)


if __name__ == "__main__":
    main()
