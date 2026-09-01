import pandas as pd
import requests


def load_fda_data(limit=1000):
    url = f"https://api.fda.gov/food/enforcement.json?limit={limit}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json().get("results", [])
    df = pd.DataFrame(data)

    if not df.empty and "recall_initiation_date" in df.columns:
        df["recall_initiation_date"] = pd.to_datetime(
            df["recall_initiation_date"],
            format="%Y%m%d",
            errors="coerce",
        )

    return df
