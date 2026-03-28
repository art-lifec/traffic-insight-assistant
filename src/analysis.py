#analysis
import requests
import pandas as pd

def load_tomtom_flow(lat, lon, api_key):
    url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"

    params = {
        "point": f"{lat},{lon}",
        "key": api_key
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return data