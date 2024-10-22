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
        rank = []
        if data and "attributes" in data:
            title_list = [point["value"] for point in data["attributes"]["item_name"]]
            description_list = [point["value"] for point in data["attributes"]["bullet_point"]]
        if data and "salesRanks" in data:
            if isinstance(data["salesRanks"], dict) and "displayGroupRanks" in data["salesRanks"]:
                for i in data["salesRanks"]["displayGroupRanks"]:
                    rank.append(str(i["rank"]))
            elif isinstance(data["salesRanks"], list):
                for group in data["salesRanks"]:
                    if "displayGroupRanks" in group:
                        for i in group["displayGroupRanks"]:
                            rank.append(str(i["rank"]))
        title_str = " ".join(title_list)
        description_str = " ".join(description_list)
        rank_int = int(rank[0]) if rank else None
        r = {
            "asin": asin,
            "title": title_str,
            "description": description_str,
            "rank": rank_int
        }
        return json.dumps(r)
    else:
        return None


result = get_asins("B000B68V6I")

print(result)
