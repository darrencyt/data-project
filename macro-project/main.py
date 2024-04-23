import yfinance as yf
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import json
from datetime import datetime, datetime, timedelta

uri = "mongodb+srv://dubook0628:08QFiZeALNs15mgc@cluster0.mvtv3jk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database("school")
collection = db.get_collection("student")

data = yf.download("SGD=X", start="2022-01-01", end="2022-12-31")
data.reset_index(inplace=True)

# Convert pandas DataFrame to JSON
data_json = json.loads(data.to_json(orient="records"))

# Insert data into MongoDB collection
collection.insert_many(data_json)

# end_date = datetime.today().strftime("%Y-%m-%d")
# yesterday = datetime.today() - timedelta(days=1)
# yesterday_str = yesterday.strftime("%Y-%m-%d")

# new_data = yf.download("SGD=X", start="2023-01-01", end="2023-01-03")
# new_data.reset_index(inplace=True)

# # Convert pandas DataFrame to JSON
# new_data_json = json.loads(new_data.to_json(orient="records"))

# # Insert data into MongoDB collection
# collection.insert_many(new_data_json)