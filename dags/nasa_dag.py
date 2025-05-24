from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from nasa_etl import (
    fetch_apod_entries,
    transform_entries,
    write_entries_csv,
) 

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="nasa_apod_etl",
    default_args=default_args,
    description="APOD ETL broken into fetch/transform/write",
    schedule_interval="@daily",
    start_date=datetime(2025, 4, 21),
    catchup=False,
    tags=["nasa", "apod"],
) as dag:

    @task(multiple_outputs=True)
    def fetch(days: int = 200):
        """Fetch the raw APOD payloads from NASA."""
        return {"entries": fetch_apod_entries(days)}

    @task()
    def transform(entries: list[dict]):
        """Clean and normalize the raw entries."""
        return transform_entries(entries)

    @task()
    def write(processed: list[dict]):
        """Write final CSV to local_fs."""
        write_entries_csv(processed, output_path="/opt/airflow/local_fs/apod.csv")

    fetched = fetch()
    cleaned = transform(fetched["entries"])
    write(cleaned)
