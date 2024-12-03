import openpyxl
import requests
import json
import pandas as pd
from openpyxl import Workbook


def get_asins(access_token, client_id, profile_id, asins, count):
    url = "https://advertising-api.amazon.com/sp/targets/products/recommendations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spproductrecommendation.v3+json',
        'Accept': 'application/vnd.spproductrecommendation.v3+json'
    }
    data = {
        "adAsins": asins,
        "count": count,
        "locale": "en_US"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        print(f"Success: {response.status_code} - {response.text}")
        # return response_json
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


profile_id = "3338272033075265"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIOQ9jeGn_NPYcYqtld3cA7KK7363KdqUBJDYcV-B36zJhyrK6Y-Y5-KniyFw8G2FKH7c692VcEm7udUvYY2NwXqhbM1LLygPuF5lxd8Kw2zCjwFqYf_YqNaRQyJPnpfs3APlYrCrraKTahjA0oiF9E7yq3rz9LY1rs8HfsLVAsl6vn4CWCGFErxbD8wEK_xxQ1wWmLbLYEEYfZYqN487LAYpDtYXT51IrdiMv-KW0YUplyxxQ7zAYaEdMrXSmtbbO-7S78S4nILvj23no4OzbGyD7ws8pEnPNKP3OR9eVcycYSvDNzvQ1qpSiOWyujbaR6I9Xw3f0P75ejC0a6F51iyTASPdDLUlghzKb_02iS13ZLBhZW2-gtPp9xeIS77R1TWZHC8kwG-OKoM_ZA5uOfxIiVmOem_SwMTbkzCregW7DUIkAvpEu7ZVTEoUMJhJy-sjgL2ASd4x86mZFD64q9ja0f1DYU41XE3P1VXWfLGcog"
asins = ['B07M7TLN6G']
count = 10
result = get_asins(access_token, client_id, profile_id, asins, count)
print(json.dumps(result, indent=4, ensure_ascii=False))

if result:
    df = pd.DataFrame(result, columns=["asins"])
    file_name = "B09BZ8VSYL-us.xlsx"
    df.to_excel(file_name, index=False)

    print(f"文件保存到{file_name}:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
else:
    print("没有相关ASIN返回")