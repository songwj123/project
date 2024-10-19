import requests
import json


def get_asins(asin):
    print(type(asin))
    url = f"http://192.168.10.160:5049/CatalogItem/{asin}"
    headers = {
        "Content-Type": "application/json"
    }
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        title_list = []
        description_list = []
        if data and "attributes" in data:
            title_list = [point["value"] for point in data["attributes"]["item_name"]]
            description_list = [point["value"] for point in data["attributes"]["bullet_point"]]
        r = {
            "asin": asin,
            "title": title_list,
            "description": description_list
        }
        return json.dumps(r)
    else:
        return None


result = get_asins("B000B68V6I")

print(result)
