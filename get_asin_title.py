import requests


def get_product_title(access_token, client_id, profile_id):
    url = "https://advertising-api.amazon.com/product/metadata"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.productmetadatarequest.v1+json',
        'Accept': 'application/vnd.productmetadataresponse.v1+json'
    }
    data = {
        "checkItemDetails": True,
        "checkEligibility": True,
        "pageSize": 1,
        "locale": "zh_CN",
        "asins": [
            "B07F7VG6Q8"
        ],
        # "cursorToken": "SUGGESTED",
        "adType": "SP",
        "pageIndex": 1,
        "sortOrder": "DESC",
        # "sortBy": "SUGGESTED"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


profile_id = "2651906346803655"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIDENVNPrOLvc2rtpmgkTZStfzSw25jFqW-wmIhwiKDmbCT-PMMtY2kePCTfqXgE8PBkSq-p7bGz8FlQpIs5zMkNvPvyRCOU1pQTQerKqwNjHbDgpy2ukAoBYCJRc1VmQD-s0_S0KOvwiJlIJdpUGyyyMXNSKVBvdUzbxnSyXvWGl-R0sN_DjHbcQ-7gXXYxeqKK6mn9sTPJ6-uXIP25Wb5hqK-x-_3gn02saGEPNXHe1s-40GGR1ogjASaa_0XxqkXliE0qs89OTYr52jaJFT9I2BJOFnaH-3olZ5NOoLPIp1PBqwrmuwlfzxVbOk6zSXSC-xvtleBLzHERVSulVtCIAe9igbf7yLg6DIdjg56vqZQPd67I_jCrLFHDyX4NyjDFI_iS22pcxRmc_jKV5l_LunhgmbcQLZyzVOKKkarEo9aEcsttfVIOdLhCuejss6RKefY_wYJEDjU00xhFupq2L"
result = get_product_title(access_token, client_id, profile_id)

print(result)
