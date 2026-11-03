# PROVENANCE: data/raw/online_retail.csv

## File in this folder

- File: online_retail.csv
- Rows: 541,909, plus a header row
- Columns: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country
- Date range in the file: 1 December 2010 to 9 December 2011
- Size: about 43 MB
- Encoding: UTF-8, read as text in the notebooks

## Canonical source

- UCI Machine Learning Repository, Online Retail II, dataset 502
- Creator: Daqing Chen
- Citation: Chen, D. (2012). Online Retail II [Dataset]. UCI Machine Learning Repository. DOI: 10.24432/C5CG6D.
- Dataset page: https://archive.ics.uci.edu/dataset/502/online+retail+ii
- Full UCI file: all transactions for a UK based, non-store online retailer between 1 December 2009 and 9 December 2011, 1,067,371 rows, file online_retail_II.xlsx, 43.5 MB, as listed on the UCI page.
- UCI description: the company mainly sells unique all-occasion gift ware, and many customers are wholesalers.

## Download actually used

- Primary download URL used by scripts/download_data.py: https://raw.githubusercontent.com/databricks/Spark-The-Definitive-Guide/master/data/retail-data/all/online-retail-dataset.csv
- This is the December 2010 to December 2011 slice of the same retailer, with the same 8 columns. It is the slice most public RFM tutorials use, and it is served as a plain CSV, with no login or key.
- Fallback URL in the script: https://github.com/dbdmg/datasciencelab/raw/master/datasets/online_retail.csv (Politecnico di Torino data science lab mirror, also 541,909 rows, same slice).
- Why a mirror was used: the direct UCI static xlsx URL returned 404 in this run, and the ucimlrepo fetch for dataset 502 raised an SSL connection error. The mirror download succeeded and its row count and dates were verified in notebook 01.

## What this means for reuse

Do not cite this folder as the full Online Retail II file. Cite it as the December 2010 to December 2011 slice, 541,909 rows, from the UCI Online Retail II retailer. If you need the 2009 year, download the full file from UCI and rerun scripts/build_processed.py and the notebooks. Monthly, cohort, and segment numbers will change, because the customer base and the reference date will change.

## Cleaning applied downstream

See scripts/build_processed.py and notebook 01. In short: drop cancellations (invoice starts with C), drop quantity or price at or below zero, drop rows with no CustomerID, add Revenue as Quantity times UnitPrice in pounds sterling. Clean result: 397,884 rows, 4,338 customers, 18,532 invoices, 8,911,407.90 pounds.

## Licence note

The UCI page lists this dataset for research and teaching use. Check the UCI dataset page for its current licence terms before commercial reuse. No customer names are in the file, and none were added here.
