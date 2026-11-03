# Applied Data Analytics End to End

A complete, beginner friendly analysis of a real online shop, from messy raw rows to customer segments, a tested forecast, and actions a small shop could try. No step is hidden. Every number in this README comes from the notebooks, and every limit is stated next to the finding it affects.

## The shop in one paragraph

This is a UK based online retailer that mainly sells unique gift ware, and many of its customers are wholesalers. The data cover December 2010 to December 2011, in this build. The shop earns most of its money in the United Kingdom, sells most in the autumn, and depends heavily on a small group of repeat customers. That is the story. The rest of this project shows the working.

## What you will learn, in order

1. How to load a real file and clean it without hiding the messy rows.
2. How to read sales over time, by month, weekday, and hour.
3. How to see where money comes from, by country and by product.
4. How to group customers with RFM: recency, frequency, and monetary value.
5. How to test a forecast before trusting it, and how to build two simple customer signals.
6. How to turn findings into actions, and how to state limits honestly.

Each idea is explained before it is used. If you are new, start at notebook 01 and read in order. If you already work with data, start at notebook 04 or 05.

## The data, stated plainly

Source: UCI Machine Learning Repository, Online Retail II, dataset 502, by Daqing Chen (2012). DOI: 10.24432/C5CG6D. Page: https://archive.ics.uci.edu/dataset/502/online+retail+ii

The full UCI file covers 1 December 2009 to 9 December 2011 and has 1,067,371 rows. This build uses the December 2010 to December 2011 slice, served as a CSV mirror, with 541,909 rows. The slice uses the same schema and the same retailer, and it is the part most public RFM tutorials use. Do not mistake this slice for the full file. The download script and data/raw/PROVENANCE.md record both facts.

Cleaning, in order: drop cancelled invoices (invoice number starts with C, 9,288 rows), drop rows with quantity or price at or below zero, drop rows with no CustomerID (132,220 rows at that step, after the earlier filters; 135,080 rows in the raw file). Clean result: 397,884 rows, 4,338 customers, 18,532 invoices, revenue of 8,911,407.90 pounds, from 1 December 2010 to 9 December 2011.

December 2011 is a partial month. Data stop on 9 December 2011, so its bar is low because most of the month is missing, not because demand collapsed.

## Key findings, with exact numbers

- Best complete month: November 2011, 1,161,817.38 pounds. Quietest complete month: February 2011, 447,137.35 pounds. Average complete month: 699,434.59 pounds.
- United Kingdom: 7,308,391.55 pounds, or 82.01 percent of clean revenue. Next: Netherlands, 285,446.34 pounds. Then EIRE, 265,545.90 pounds.
- Top product by revenue: PAPER CRAFT, LITTLE BIRDIE, 168,469.60 pounds. Next: REGENCY CAKESTAND 3 TIER, 142,592.95 pounds. POSTAGE (77,803.96 pounds) is a delivery charge, not a gift, and is flagged in notebook 03.
- Median customer: last ordered 51 days before the reference date (10 December 2011), placed 2 orders, spent 674.48 pounds. The mean is far higher, because a few wholesale buyers distort it, so quote the median for a typical customer.
- Champions: 797 customers (18.4 percent) account for 5,767,945.43 pounds (64.7 percent of revenue). Champions plus Loyal customers: 37.5 percent of customers, 82.6 percent of revenue.
- Repeat customers: 65.58 percent ordered more than once. One time customers: 34.42 percent.
- Quiet customers: 33.4 percent had recency over 90 days, and 19.8 percent over 180 days, at the reference date.
- Forecast test: a 3 month moving average missed September, October, and November 2011 by 33.3, 29.5, and 24.3 percent, for an average miss (MAPE) of 29.0 percent. It missed low each time, because sales were rising. The next month forecast on that method is 1,051,324.85 pounds. Quote it only with the 29.0 percent miss.
- Original metric, Recency Gap Ratio: days since last order divided by the median gap between that customer's own past orders. A ratio above 2 means the customer waited more than twice as long as usual. Among 2,760 customers with a usable ratio (at least two orders on different days), 18.6 percent are above 2, and 12.2 percent are above 3. This is a warning signal, not a proven churn prediction.
- Simple customer value estimate: average order value times orders per year times 2 years. Median for repeat customers: 3,997.70 pounds. The mean, 9,723.01 pounds, is distorted by one very large wholesale buyer, so do not quote the mean. This estimate assumes the past rate continues, which it may not, and it ignores costs.

## Notebooks

- 01_load_and_clean.ipynb: load, count missing values, clean step by step.
- 02_sales_trends.ipynb: monthly revenue and orders, weekday, hour.
- 03_products_and_countries.ipynb: country shares, top products.
- 04_rfm_segmentation.ipynb: RFM scores and six segments.
- 05_forecast_and_churn_clv.ipynb: 3 month average forecast backtest, Recency Gap Ratio, customer value estimate.
- 06_story_and_actions.ipynb: cohorts, story in five sentences, actions, limits.

Each notebook starts with a pip install cell and was executed end to end with zero cell errors.

## Charts

17 charts are in charts/, and copies are in docs/charts/ for the story site. They are: missing values, cleaning funnel, monthly revenue, monthly orders, weekday revenue, hour revenue, top 10 countries, UK versus rest, top 10 products, segment customers, segment revenue, recency histogram, forecast backtest, gap ratio, CLV by segment, new customers by cohort month, repeat versus one time customers.

## How to rebuild it

```bash
python scripts/download_data.py
python scripts/build_processed.py
```

Then open the notebooks in order and run all cells. Or run:

```bash
bash scripts/rebuild_all.sh
```

That script rebuilds the processed tables and re-executes all six notebooks. It needs Python 3.10 or later and the packages in requirements.txt.

## The original repo, and what this folder builds on

This folder is a fresh local build. It does not delete or overwrite any file from the original repo, github.com/jwavalosq/datanalytics. The original repo, as briefed, is a skeleton with no complete project. Its existing files, preserved in the original repo and not copied over here, are: a small model.py, a Streamlit stub streamlit_app.py, plot.png, ejemplo.R, a README stub, and empty course folders. This project matches the repo description, educational and practical resources for Applied Data Analytics, by turning that skeleton idea into one finished end to end example. This project was built locally and then published to this repo.

## Credits and methods, not just a clone

The dataset and the RFM idea are well known public methods, and this project credits them rather than claiming them as new. The RFM quartile method follows the standard public RFM teaching approach used in many tutorials on this same dataset. The forecast is a standard 3 month moving average, chosen because it is transparent. The original contributions are: the Recency Gap Ratio, which compares each customer with their own past rhythm instead of one fixed cutoff; the plain word story that carries the limits with each number; and the combined end to end chain from download script to processed tables to story site in one folder. No data, map, or test was faked. Where a method is weak, the notebook says so.

## Limits, in short

Data end in December 2011, so nothing here describes shopping today. Customer counts exclude rows with no CustomerID. RFM cutoffs are a teaching choice. The forecast has no seasonality model, no price model, and no promotion data. The gap ratio and the value estimate are signals, not predictions or booked revenue. Many customers are wholesalers, so large orders are normal for them.
