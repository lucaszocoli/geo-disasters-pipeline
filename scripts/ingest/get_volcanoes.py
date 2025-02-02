import requests
import pandas as pd
from config.settings import NASA_EONET_API_URL

def get_volcanoes():
    response = requests.get(NASA_EONET_API_URL)
    data = response.json()
    
    volcanoes = []
    for event in data["events"]:
        if "volcano" in event["categories"][0]["title"].lower():
            volcanoes.append({
                "id": event["id"],
                "event_type": "volcano",
                "magnitude": None,
                "place": event["title"],
                "time": event["geometry"][0]["date"],
                "longitude": event["geometry"][0]["coordinates"][0],
                "latitude": event["geometry"][0]["coordinates"][1],
                "depth": None
            })
    
    return pd.DataFrame(volcanoes)

if __name__ == "__main__":
    df = get_volcanoes()
    df.to_csv("data/raw/volcanoes.csv", index=False)
    print("Dados de vulcões salvos!")
