import openpyxl
import requests
import json
import pandas as pd
from openpyxl import Workbook


def get_asins(access_token, client_id, profile_id, asins, count):
    url = "https://advertising-api-eu.amazon.com/sp/targets/products/recommendations"
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
        "locale": "it_IT"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        # return response_json
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


profile_id = "1322367844724023"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIGChn2kdUs5740ET5ZtOpZOkXdS-9KMm7kdSW6CGqujVrxrqz3E5orXZTaMt63sfFrhaEAp02foaUCjHaoHYpKEM_I4Bd2ZqJDbfxF67H7VKK5fOmXcE2APY1WZsTER5uP5cd6gk8NBgbWrP07ZUV3flnWNvxhhfIKQpxS_pwJ_MOzapOhAjMdgUrNbePtd64YPcT4SPZ5VF2CURIBo0nI-IbjoPl81sfefpBExpaLfL7p5AaqaGd7MWXs_c5FGTm2b8hSrZIoHIBeVsvx_j_8k_vSmMU-6YFpRXZUIveWPnT-VDxhyp2-UJbqGw6BxIikPrtFPV1Ma0Gj4z29gq-m9HaL-fo2EXUfhUqUcjice7fF7SqYjb92hZX5rL56XYtCZShlY4ucRn6o3pITRGUsyZ4GWNrLkvVl6ujk-Zi33mxJhFca13NOCRM80G1p9PbFhQQeXy-6PKIJYqPvXsLDdW7MAoW4fh8ksQ5HhSyG1X7JiCTKBkgwSAqTky3M8808CpltulrCUmXGlYHyM091IbAhw70LroaJHjjMKP5oMjBA"
asins = ['B0D6B7MD6Z']
count = 47
result = get_asins(access_token, client_id, profile_id, asins, count)
print(json.dumps(result, indent=4, ensure_ascii=False))

if result:
    df = pd.DataFrame(result, columns=["asins"])
    file_name = "B0D6B7MD6Z-IT.xlsx"
    df.to_excel(file_name, index=False)

    print(f"文件保存到{file_name}:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
else:
    print("No ASINs returned.")