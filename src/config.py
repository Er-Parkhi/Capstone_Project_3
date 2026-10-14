import os

storage_account_name = "azstore01"
container_name = "uber-taxi"
storage_account_key = os.environ["AZURE_STORAGE_ACCOUNT_KEY"]
foundry_api_key = os.environ["FOUNDRY_API_KEY"]
foundry_endpoint = "https://my-azureai-foundry-resource.services.ai.azure.com/api/projects/my-azureai-foundry"
foundry_model = "gpt-5-mini"

storage_base = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net"

source_path = f"{storage_base}/ncr_ride_bookings.csv"
base_path = f"{storage_base}/output"
bronze_path = f"{base_path}/bronze"
silver_path = f"{base_path}/silver"

gold_daily_path = f"{base_path}/gold/daily_trip_summary"
gold_location_path = f"{base_path}/gold/location_trip_summary"
gold_payment_path = f"{base_path}/gold/payment_type_trip_summary"

# "/Workspace/uber-taxi-agentic-etl/data"
