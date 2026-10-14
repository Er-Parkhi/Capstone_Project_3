# Uber Taxi Agentic ETL

Databricks ETL project that processes Uber taxi bookings into Bronze, Silver,
and Gold Delta datasets, with data-quality checks and agent-driven analytics.

## Configuration

Set these environment variables in the runtime before importing the project:

- `AZURE_STORAGE_ACCOUNT_KEY` — Azure Storage account key.
- `FOUNDRY_API_KEY` — Microsoft Foundry API key.

The source CSV and output Delta paths are configured in `src/config.py`.
The notebook in `notebooks/uber-etl.ipynb.py` demonstrates running the pipeline
and the LangGraph agent workflow in Databricks.
