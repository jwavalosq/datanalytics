# BUILD REPORT: Applied Data Analytics End to End

## Folder

Local folder: ~/workspace/repo-builds/datanalytics-project/

Nothing was published, pushed, posted, or signed into. Local build only.

## Original repo files used, and what was preserved

Original repo: github.com/jwavalosq/datanalytics, as briefed. Existing files, preserved in the original repo and not deleted or overwritten: small model.py, Streamlit stub streamlit_app.py, plot.png, ejemplo.R, README stub, and empty course folders.

This build works in a fresh local folder, so none of those files were touched. No original file was copied into this folder as a deliverable, because the brief was to build one complete project the skeleton lacked, not to edit the stub files in place. The repo description, educational and practical resources for Applied Data Analytics, set the tone: plain words, a full chain, and actions a learner can reuse.

## Files produced

- notebooks/01_load_and_clean.ipynb
- notebooks/02_sales_trends.ipynb
- notebooks/03_products_and_countries.ipynb
- notebooks/04_rfm_segmentation.ipynb
- notebooks/05_forecast_and_churn_clv.ipynb
- notebooks/06_story_and_actions.ipynb
- charts/: 17 PNG charts, numbered 01 to 17 (list in README.md)
- docs/index.html, plus chart copies in docs/charts/
- data/raw/online_retail.csv (541,909 rows, 43 MB)
- data/raw/PROVENANCE.md
- data/processed/clean_transactions.csv (397,884 rows)
- data/processed/monthly_sales.csv
- data/processed/rfm_segments.csv (4,338 customers)
- data/processed/customer_gap_clv.csv
- data/processed/country_sales.csv
- data/processed/product_sales.csv
- data/processed/forecast_backtest.csv
- scripts/download_data.py
- scripts/build_processed.py
- scripts/build_notebooks.py
- scripts/rebuild_all.sh
- requirements.txt
- .gitignore
- README.md
- BUILD_REPORT.md (this file)

## What ran

1. Created a Python virtual environment in .venv/ and installed pandas, numpy, matplotlib, seaborn, scikit-learn, openpyxl, jupyter, nbconvert, and ucimlrepo.
2. Downloaded the data with the Databricks CSV mirror (see PROVENANCE.md). Verified shape: 541,909 rows, 8 columns.
3. Ran scripts/build_processed.py. Output: raw rows 541,909, cancelled rows 9,288, missing CustomerID rows removed at the customer step 132,220, clean rows 397,884, clean revenue 8,911,407.90 pounds, customers 4,338, reference date 10 December 2011.
4. Generated six notebooks with scripts/build_notebooks.py, each with a top pip install cell.
5. Executed all six notebooks end to end with jupyter nbconvert. Result: zero cell errors in all six notebooks. Charts were written by the notebooks to charts/.
6. Fixed two summary numbers after execution, by editing notebook markdown (not outputs): gap ratio figures corrected from an early estimate (15.3 and 9.5 percent) to the executed values (18.6 and 12.2 percent), and median monetary corrected to 674.48 pounds and median CLV estimate to 3,997.70 pounds, to match executed outputs exactly. The builder script was fixed to match, so a rebuild does not reintroduce the old numbers.
7. Copied charts to docs/charts/ and built docs/index.html.
8. Checked every file for the em dash character, excluding .venv/. Result: no em dash found in project files. See the check command in scripts/rebuild_all.sh notes and the final check below.

## What failed or was approximated

- UCI direct download failed on first try. The ucimlrepo fetch for dataset 502 raised a connection error (SSL EOF) in this environment, and the direct static xlsx URL returned 404. The build therefore uses the Databricks CSV mirror of the same retailer and schema, with the full UCI file clearly distinguished from the slice used. This is an approximation of source, not of numbers: every number in the notebooks comes from the downloaded slice itself, and the slice size and dates are stated.
- The full UCI Online Retail II file (1,067,371 rows, December 2009 to December 2011) was NOT used. The slice used is December 2010 to December 2011, 541,909 rows. Any reader who needs the 2009 year must download the full file from UCI and rerun the notebooks. The cleaning code does not depend on the year range, but the monthly and cohort numbers would change.
- Forecast is approximated by design. A 3 month moving average is simple and transparent, and its backtest miss is 29.0 percent. No seasonal, price, or promotion model was fitted, because the file has no promotion or cost fields, and a fancier model would overclaim on 12 complete months.
- Recency Gap Ratio is approximated by design. It needs at least two orders on different days. That gives 2,760 of 4,338 customers. One time buyers (1,493 customers) and 85 repeat customers whose orders fall on a single day pattern with a zero median gap get no ratio. No ratio was invented for them.
- Customer value estimate is approximated by design. Formula: average order value times orders per year times 2 years, with orders per year from first order to the reference date. It assumes the past rate continues, ignores costs, and is reported as a median (3,997.70 pounds for repeat customers) because the mean (9,723.01 pounds) is distorted by a very large wholesale buyer.
- RFM segments are a teaching choice, not a validated business rule. Quartile scores and the segment thresholds in notebook 04 would move customers between groups if changed. Counts and revenue shares are shown so the choice can be judged.
- Country name EIRE is kept as written in the source file. It refers to Ireland in this dataset context, but the file label is not changed, to avoid silently renaming source data.

## What was cut, and why

- No map. Country data in this file are names, not coordinates, and a map would need a shapefile or geocoding step that could introduce errors. Country results are shown as bars instead, which is honest and readable.
- No market basket analysis. It is a natural next step for this dataset, but the brief asked for trends, RFM, forecasting, and one original metric, and six notebooks already cover those plus cohorts and actions. Basket work is listed as a next step, not faked as done.
- No machine learning classifier for churn. There is no future label in this file: no one knows, from the file alone, who truly churned after December 2011. A classifier trained on a made up label would be fake validation. The gap ratio is therefore presented as a signal, not a prediction.
- No December 2011 full month comparison. December 2011 is partial (to 9 December), so it is excluded from complete month averages and from forecast training. It appears in charts with a partial label, not as a full month.
- No Streamlit app in this folder. The original repo has a Streamlit stub, but this build is notebooks plus a static story site, as briefed. A Streamlit version would be a separate next step, reusing data/processed/.
- No 2009 data, no external price, weather, or promotion data, and no customer names. The file has no names, and none were invented.

## Key verified findings (all from executed notebooks)

- Clean: 397,884 rows, 4,338 customers, 18,532 invoices, 8,911,407.90 pounds.
- November 2011: 1,161,817.38 pounds (best complete month). February 2011: 447,137.35 pounds (quietest complete month).
- United Kingdom: 7,308,391.55 pounds, 82.01 percent. Netherlands: 285,446.34 pounds. EIRE: 265,545.90 pounds.
- Top product: PAPER CRAFT, LITTLE BIRDIE, 168,469.60 pounds.
- Champions: 797 customers, 5,767,945.43 pounds, 64.7 percent of revenue. Champions plus Loyal: 82.6 percent of revenue from 37.5 percent of customers.
- Median customer: recency 51 days, frequency 2 orders, monetary 674.48 pounds.
- Repeat customers: 65.58 percent. One time: 34.42 percent.
- Forecast backtest MAPE: 29.0 percent. Next month forecast (3 month average): 1,051,324.85 pounds.
- Gap ratio above 2: 18.6 percent of 2,760 customers with a usable ratio. Above 3: 12.2 percent.
- Median 2 year CLV estimate, repeat customers: 3,997.70 pounds.

## What could not be verified

- The full UCI file was not downloaded in this run, so its 1,067,371 row count and 2009 to 2011 range are cited from the UCI dataset page and from public descriptions of dataset 502, not from a file inspected here. The slice used here was inspected directly.
- Whether any individual customer is a wholesaler or a consumer cannot be verified from this file, because the file has no customer type field. The retailer description (many customers are wholesalers) comes from the UCI dataset description, and it is attributed as such, not inferred per customer.
- Causes of the autumn sales rise (for example, holiday shopping) cannot be verified from sales rows alone. The README and notebooks describe timing only, and do not claim a cause.
- No future churn outcome exists in the file, so the gap ratio cannot be validated as a churn predictor here. It is labelled a signal throughout.

## Rebuild

```bash
bash scripts/rebuild_all.sh
```

That rebuilds processed tables and re-executes all notebooks. Check for the banned character with:

```bash
python3 -c "import pathlib,sys; bad=[str(p) for p in pathlib.Path('.').rglob('*') if p.is_file() and '.venv' not in str(p) and chr(8212) in p.read_text(errors='ignore')]; print(bad or 'no em dash found')"
```

Note: exclude .venv/ from that check, as required.
