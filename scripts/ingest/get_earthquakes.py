import requests
import pandas as pd
from config.settings import USGS_API_URL

def get_earthquakes(start_date="2024-02-01", end_date="2024-02-02", min_magnitude=2.5):
    params = {
        "format": "geojson",
        "starttime": start_date,
        "endtime": end_date,
        "minmagnitude": min_magnitude
    }
    
    response = requests.get(USGS_API_URL, params=params)
    data = response.json()
    
    earthquakes = []
    for feature in data["features"]:
        props = feature["properties"]
        earthquakes.append({
            "id": feature["id"],
            "event_type": "earthquake",
            "magnitude": props["mag"],
            "place": props["place"],
            "time": pd.to_datetime(props["time"], unit="ms"),
            "longitude": feature["geometry"]["coordinates"][0],
            "latitude": feature["geometry"]["coordinates"][1],
            "depth": feature["geometry"]["coordinates"][2]
        })
    
    return pd.DataFrame(earthquakes)

if __name__ == "__main__":
    df = get_earthquakes()
    df.to_csv("data/raw/earthquakes.csv", index=False)
    print("Dados de terremotos salvos!")
