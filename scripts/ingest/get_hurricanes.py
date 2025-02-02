import requests
import pandas as pd
from config.settings import NASA_EONET_API_URL

def get_hurricanes():
    response = requests.get(NASA_EONET_API_URL)
    data = response.json()
    
    hurricanes = []
    for event in data["events"]:
        if "storm" in event["categories"][0]["title"].lower():
            hurricanes.append({
                "id": event["id"],
                "event_type": "hurricane",
                "magnitude": None,
                "place": event["title"],
                "time": event["geometry"][0]["date"],
                "longitude": event["geometry"][0]["coordinates"][0],
                "latitude": event["geometry"][0]["coordinates"][1],
                "depth": None
            })
    
    return pd.DataFrame(hurricanes)

if __name__ == "__main__":
    df = get_hurricanes()
    df.to_csv("data/raw/hurricanes.csv", index=False)
    print("Dados de furacões salvos!")
