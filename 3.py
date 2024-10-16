import json

import requests


def get_keyword(asin):
    response = requests.get(f"http://192.168.10.160:5049/CatalogItem/{asin}")
    if response.status_code == 200:
        data = response.json()
        print(json.loads(data))


asins = "B0D8Q15LPC"
get_keyword(asins)
