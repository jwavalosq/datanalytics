# Applied Data Analytics End to End: One Real Shop, From Messy Rows to Actions

I took a real online shop's real sales data and turned it into a complete analytics story, from messy raw rows to customer segments, a tested forecast, and actions a small shop could actually try. Nothing is hidden. Every number in this README comes from the notebooks, and every limit is stated next to the finding it affects.

Read the story version: https://jwavalosq.github.io/datanalytics/

## The question I started with

A UK online retailer sells mostly unique gift ware, and many of its customers are wholesalers. I wanted to answer the questions a shop owner would actually ask: when do we sell, where does the money come from, who are our best customers, can we forecast next month, and which customers are quietly drifting away? I also wanted the project to teach. If you are new to data analytics, you can follow every step in order and learn the methods as you go. If you already work with data, you can jump straight to the customer segments and the forecast test.

## Why it matters

Small shops live or die on a small group of repeat customers, and they waste money when they guess at the future instead of testing a forecast first. This project shows both ideas with real numbers. It also shows the unglamorous part of analytics that most tutorials skip: cleaning messy data without hiding the messy rows, and saying plainly what a method cannot prove.

## What I did, step by step

First, I loaded the data and cleaned it in the open. The source is the UCI Machine Learning Repository, Online Retail II, dataset 502, by Daqing Chen (2012). The full UCI file covers 1 December 2009 to 9 December 2011 and has 1,067,371 rows. This build uses the December 2010 to December 2011 slice, 541,909 rows, served as a CSV mirror. It uses the same schema and the same retailer, and it is the part most public RFM tutorials use. Do not mistake this slice for the full file. The download script and `data/raw/PROVENANCE.md` record both facts. The raw 45 MB CSV is excluded from the repo, and you can re-download it with the script.

Cleaning, in order: I dropped cancelled invoices (invoice number starts with C, 9,288 rows), dropped rows with quantity or price at or below zero, and dropped rows with no CustomerID (132,220 rows at that step, after the earlier filters; 135,080 rows in the raw file). The clean result is 397,884 rows, 4,338 customers, 18,532 invoices, and revenue of 8,911,407.90 pounds, from 1 December 2010 to 9 December 2011. December 2011 is a partial month. Data stop on 9 December 2011, so its bar is low because most of the month is missing, not because demand collapsed.

Second, I read sales over time, by month, weekday, and hour. Third, I traced where money comes from, by country and by product. Fourth, I grouped customers with RFM: recency, frequency, and monetary value. Fifth, I tested a forecast before trusting it, and built two simple customer signals. Sixth, I turned the findings into actions, and wrote down the limits honestly.

The work is six notebooks and 17 charts, each notebook executed end to end with zero cell errors.

## What I found

**Sales rise into autumn.** The best complete month was November 2011, at 1,161,817.38 pounds. The quietest complete month was February 2011, at 447,137.35 pounds. The average complete month was 699,434.59 pounds.

**The shop earns most of its money at home.** The United Kingdom brought in 7,308,391.55 pounds, or 82.01 percent of clean revenue. Next came the Netherlands, at 285,446.34 pounds, then EIRE, at 265,545.90 pounds.

**One product leads by a wide margin.** The top product by revenue was PAPER CRAFT, LITTLE BIRDIE, at 168,469.60 pounds. Next was REGENCY CAKESTAND 3 TIER, at 142,592.95 pounds. POSTAGE, at 77,803.96 pounds, is a delivery charge, not a gift, and it is flagged in notebook 03.

**A small group of customers carries the shop.** Champions are 797 customers (18.4 percent) who account for 5,767,945.43 pounds (64.7 percent of revenue). Champions plus Loyal customers are 37.5 percent of customers and 82.6 percent of revenue. The median customer last ordered 51 days before the reference date (10 December 2011), placed 2 orders, and spent 674.48 pounds. I quote the median for a typical customer, because the mean is far higher and a few wholesale buyers distort it.

**Most customers come back.** Repeat customers are 65.58 percent of customers. One time customers are 34.42 percent. But 33.4 percent of customers had a recency over 90 days, and 19.8 percent over 180 days, at the reference date. Those quiet customers are the ones to check on first.

**The forecast must carry a warning label.** A 3 month moving average missed September, October, and November 2011 by 33.3, 29.5, and 24.3 percent, for an average miss (MAPE) of 29.0 percent. It missed low each time, because sales were rising. The next month forecast on that method is 1,051,324.85 pounds. Quote it only with the 29.0 percent miss.

**My original metric: the Recency Gap Ratio.** A fixed 90 day cutoff treats a weekly buyer and a yearly buyer the same way, and that is unfair. My Recency Gap Ratio compares each customer with themselves: days since last order divided by the median gap between that customer's own past orders. A ratio above 2 means the customer waited more than twice as long as usual. Among 2,760 customers with a usable ratio (at least two orders on different days), 18.6 percent are above 2, and 12.2 percent are above 3. This is a warning signal, not a proven churn prediction.

**A simple customer value estimate.** Average order value times orders per year times 2 years gives a median of 3,997.70 pounds for repeat customers. The mean, 9,723.01 pounds, is distorted by one very large wholesale buyer, so do not quote the mean. This estimate assumes the past rate continues, which it may not, and it ignores costs.

## What it means, and who it helps

For a shop owner, the priorities are clear. Protect the Champions first, because they carry 64.7 percent of revenue. Check in with stretched repeat buyers, those with a gap ratio above 2, before offering a discount. Help recent buyers place a second order, because turning a recent buyer into a second buyer is the cheapest growth in this data. Test one non UK market properly, starting with the Netherlands or EIRE. And staff and stock for Thursday, midday, and the autumn peak.

For a learner, this project is a full end to end example you can rerun yourself: load a real file, clean it without hiding anything, find the story in time and geography, segment customers, test a forecast honestly, and turn findings into actions. The RFM quartile method follows the standard public RFM teaching approach used in many tutorials on this same dataset. The forecast is a standard 3 month moving average, chosen because it is transparent. My original contributions are the Recency Gap Ratio, the plain word story that carries the limits with each number, and the combined chain from download script to processed tables to story site in one folder.

## How to run it yourself

```bash
python scripts/download_data.py
python scripts/build_processed.py
```

Then open the notebooks in order and run all cells. Or run:

```bash
bash scripts/rebuild_all.sh
```

That script rebuilds the processed tables and re-executes all six notebooks. It needs Python 3.10 or later and the packages in `requirements.txt`.

The notebooks, in order:

1. `01_load_and_clean.ipynb`: load, count missing values, clean step by step.
2. `02_sales_trends.ipynb`: monthly revenue and orders, weekday, hour.
3. `03_products_and_countries.ipynb`: country shares, top products.
4. `04_rfm_segmentation.ipynb`: RFM scores and six segments.
5. `05_forecast_and_churn_clv.ipynb`: 3 month average forecast backtest, Recency Gap Ratio, customer value estimate.
6. `06_story_and_actions.ipynb`: cohorts, story in five sentences, actions, limits.

The 17 charts are in `charts/`, with copies in `docs/charts/` for the story site: missing values, cleaning funnel, monthly revenue, monthly orders, weekday revenue, hour revenue, top 10 countries, UK versus rest, top 10 products, segment customers, segment revenue, recency histogram, forecast backtest, gap ratio, CLV by segment, new customers by cohort month, repeat versus one time customers.

## What the limits are

I state these plainly, because they shape every finding above.

- Data end in December 2011, so nothing here describes shopping today.
- This build uses the December 2010 to December 2011 slice, not the full 2009 to 2011 file. Anyone who needs the 2009 year must download the full file from UCI and rerun the notebooks.
- Customer counts exclude rows with no CustomerID.
- RFM cutoffs are a teaching choice, not a validated business rule.
- The forecast has no seasonality model, no price model, and no promotion data. Its backtest miss is 29.0 percent.
- The gap ratio and the value estimate are signals, not predictions or booked revenue.
- Many customers are wholesalers, so large orders are normal for them. The file has no customer type field, so I cannot verify per customer who is a wholesaler.
- No map, because country data in this file are names, not coordinates. No market basket analysis and no churn classifier: basket work is a next step, and there is no true future churn label in this file, so a classifier would be fake validation.

The original repo was a skeleton with no complete project: a small `model.py`, a Streamlit stub `streamlit_app.py`, `plot.png`, `ejemplo.R`, a README stub, and empty course folders. Those files were preserved in the repo and not deleted or overwritten. This project matches the repo description, educational and practical resources for Applied Data Analytics, by turning that skeleton idea into one finished end to end example. Full detail is in `BUILD_REPORT.md`.
