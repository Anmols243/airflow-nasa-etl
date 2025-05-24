import requests
import pandas as pd
from datetime import datetime, timedelta
from airflow.models import Variable

def fetch_apod_entries(days: int = 200) -> list[dict]:

    api_key = Variable.get("NASA_API_KEY")

    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=days - 1)

    url = (
        "https://api.nasa.gov/planetary/apod?"
        f"api_key={api_key}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
    )
    
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def transform_entries(raw: list[dict]) -> list[dict]:
    records = []
    for entry in raw:
        records.append({
            "date": entry.get("date"),
            "title": entry.get("title"),
            "explanation": entry.get("explanation"),
            "url": entry.get("url"),
            "hdurl": entry.get("hdurl"),
            "media_type": entry.get("media_type"),
        })
    return records


def write_entries_csv(records: list[dict], output_path: str) -> None:
    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False)
