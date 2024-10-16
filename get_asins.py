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
        # return response_json
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


profile_id = "2651906346803655"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIFZHPKHqXAlri2qmPLd_ms7npdsAJdMRPQT1-pFE9yVaZGMjClaAQsoAeG9NfZ4BuYOmntBWjGUZtR2oSJ6qZ3-U8GVn7MWVeQfidpUBBhfgXR2DBPHXTekGFireBXIbDb72wTcE-LyiUG5JVNPQoqBjdZPKfdgMUalcf31lVqM3i2b3PgU9pq7bboSQkn-5SpyF1s_D2VFU14To3AE1vY6yr6DhONjo4h7ZGJHs-pbADiYkKJG_i6cjcMBTAnA8LadZ057UswqQs3s1Vi82Um9R-dgDbGS6qsZFU8yPcGPWTKQ9UNM24qKjmWN5t8fTaUTTwJkUFAtKjVIbqMAvRWshismHSZWfk3lm6cMODDzeLBYf9O8q-txhfya16ZKlwQ5RU22tuByI1rcI4wyzhCpPVmMIhGeSUiavTuLaAlRHZMXFpNRK5AwKJFKzsobELfgxBo5fCM-xwLQmDAJMM71C"
asins = ['B071KW9GTT']
count = 47
result = get_asins(access_token, client_id, profile_id, asins, count)
print(json.dumps(result, indent=4, ensure_ascii=False))

if result:
    df = pd.DataFrame(result, columns=["asins"])
    file_name = "1014-B071KW9GTT.xlsx"
    df.to_excel(file_name, index=False)

    print(f"文件保存到{file_name}:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
else:
    print("No ASINs returned.")