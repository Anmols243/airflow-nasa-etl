# NASA APOD ETL Pipeline

## What it is
An Airflow ETL pipeline that pulls the NASA Astronomy Picture of the Day (APOD) for the last 200 days and writes a CSV to a local mount.

## Project Structure
project/ 
├── dags/ # Your Airflow DAG files 
|    ├── nasa_dag.py # DAG definition │
|    └── nasa_etl.py # ETL logic for NASA API 
├── docker-compose.yaml # Docker configuration 
├── .env.example # Environment variable template 
├── .gitignore # Git ignore rules 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation

## Prerequisites
- Docker and Docker Compose
- Git
- NASA API key (get it from https://api.nasa.gov/)

## Getting Started

1. Clone the repository:
bash
git clone https://github.com/your-username/airflow-nasa-etl.git
cd airflow-nasa-etl

2. Set up environment:
Copy .env.example to .env
bash
cp .env.example .env
Update the AIRFLOW_UID in .env if needed (default is 50000)

3. Start Airflow:
bash
docker-compose up -d

4. Configure NASA API Key:
Navigate to Airflow UI: http://localhost:8080
Go to Admin -> Variables
Add a new variable:
Key: NASA_API_KEY
Value: Your NASA API key from api.nasa.gov

5. Access Airflow:
URL: http://localhost:8080
Default credentials:
   Username: airflow
   Password: airflow

6. Run the Pipeline:
Navigate to DAGs view
Find 'nasa_etl' DAG
Unpause the DAG
Trigger manually or wait for scheduler

Output
The pipeline will create a CSV file containing:

Date
Title
Explanation
URL
HD URL
Media Type

for the last 200 days of NASA's Astronomy Picture of the Day.

Troubleshooting:

If you get a 403 error, verify your NASA API key is correctly set in Airflow Variables
Make sure all containers are running: docker-compose ps
Check logs in Airflow UI for detailed error messages

Development:

Dependencies are managed in requirements.txt
Add any new Python packages to requirements.txt
DAG files should be placed in the dags/ directory
