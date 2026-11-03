"""Download the Online Retail data used in this project.

Primary source: UCI Machine Learning Repository, Online Retail II,
dataset 502, Chen (2012), DOI 10.24432/C5CG6D.
Canonical page: https://archive.ics.uci.edu/dataset/502/online+retail+ii

This build uses the December 2010 to December 2011 slice of that
retailer, the same schema and the same UK based gift retailer, served
as a plain CSV mirror by Databricks in the Spark Definitive Guide
materials. The full UCI file covers December 2009 to December 2011
and has 1,067,371 rows. The mirror used here has 541,909 rows and
covers December 2010 to December 2011. That difference is stated in
PROVENANCE.md and in the README, so no reader mistakes this slice
for the full two year file.

No login or key is needed. Run from the project root:
    python scripts/download_data.py
"""
import sys
import urllib.request
from pathlib import Path

URLS = [
    "https://raw.githubusercontent.com/databricks/Spark-The-Definitive-Guide/master/data/retail-data/all/online-retail-dataset.csv",
    "https://github.com/dbdmg/datasciencelab/raw/master/datasets/online_retail.csv",
]
OUT = Path(__file__).resolve().parent.parent / "data" / "raw" / "online_retail.csv"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    last_error = None
    for url in URLS:
        print("Trying:", url)
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=180) as response:
                data = response.read()
            OUT.write_bytes(data)
            print("Saved", OUT, "bytes:", len(data))
            return 0
        except Exception as exc:  # try the next mirror
            last_error = exc
            print("Failed:", type(exc).__name__, exc)
    print("All download mirrors failed:", last_error)
    return 1


if __name__ == "__main__":
    sys.exit(main())
