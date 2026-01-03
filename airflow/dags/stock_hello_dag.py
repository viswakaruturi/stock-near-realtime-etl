from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello_stock_pipeline():
    print("Hello from the stock near real-time ETL pipeline!")


with DAG(
    dag_id="stock_hello_world",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None, 
    catchup=False,
    tags=["phase-1", "sanity-check"],
) as dag:

    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=hello_stock_pipeline,
    )
