#Analysis
import requests
import pandas as pd

def load_telraam_data():
    url = "https://telraam-api.net/ldes/observations/by-location"

    headers = {
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()

    # Telraam LDES data zit in 'member'
    records = data.get("member", [])

    # Omzetten naar DataFrame
    df = pd.json_normalize(records)

    return df
