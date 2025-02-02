import json

with open("config/db_connections.json", "r") as f:
    data = json.load(f)

DB_USER = data["user"]
DB_PASSWORD = data["password"]
DB_HOST = data["host"]
DB_PORT = data["port"]
DB_DATABASE = data["database"]

USGS_API_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
NASA_EONET_API_URL = "https://eonet.gsfc.nasa.gov/api/v3/events"
