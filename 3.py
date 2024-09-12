import requests
import json
import pandas as pd


def get_keyword_recommendations(asins, access_token, client_id, profile_id, host):
    request_payload = {
        "countryCodes": {
            "asins": asins,
        },
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "maxRecommendations": 200,  # 最大推荐数量
        "sortDimension": "CLICKS",  # 排序维度，使用 {“CONVERSIONS", "CLICKS"} 进行排序
        "locale": "en_US",  # 语言设置
        "biddingStrategy": "AUTO_FOR_SALES",  # 出价策略
        "bidsEnabled": True,  # 是否启用出价建议
        # "matchType": "EXACT"  # 匹配类型(EXACT，PHRASE，BROAD)
    }

    url = f"{host}/sp/global/targets/keywords/recommendations/list"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v5+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v5+json'
    }

    try:
        response = requests.post(url=url, headers=headers, json=request_payload)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}


def save_to_excel(data, filename):
    # 展开数据
    expanded_data = []
    for item in data:
        expanded_item = item.copy()
        # 展开 suggestedBid 字段
        suggested_bid = expanded_item.pop('suggestedBid', {})
        expanded_item.update({
            'suggestedBid_rangeStart': suggested_bid.get('rangeStart'),
            'suggestedBid_rangeMedian': suggested_bid.get('rangeMedian'),
            'suggestedBid_rangeEnd': suggested_bid.get('rangeEnd'),
            'suggestedBid_bidRecId': suggested_bid.get('bidRecId')
        })
        # 添加到列表中
        expanded_data.append(expanded_item)

    # 创建 DataFrame
    df = pd.DataFrame(expanded_data)

    # 保存到 Excel 文件
    df.to_excel(filename, index=False)
    print(f"数据已保存到 {filename}")


asins = [
    'B0CCT1F19X'
]
profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIMQ4m4qNTrBW7Gr9PXGxu8OoCoidYD5JktHHbykJn6goUyzwMPI-9jQBNUH5Nii-xSZhMjAniwY6dXZoqfrdHXWw9oLNq3BLI-9YmB1y1YFDd4e83s9iKz4cEqqgosVTftnVydEz8a4EICWKRDHFNWcqIwK_cdwSPLqdTfstt2k_WuWgWA_wESUE-z-In3pEVCQ2N7lr-D5pmAimIS598MLdXecdWHKMFQWau6ziJSaLQ6wTA1X4hYK2Trh2EOiHfw6JYj3KIxG1sxx-ehRGVoFRMgH6Vm0Mu3WHkEazdzs99WTsPPQkSF-ueMb6BkPZncNNtaYgP4gV6kotTMwceWts67dEHrp-feJ7TP9iERtM4oU8R4lRi37zIYTMBBGD9tFPebNO3vsWmdltWfscjuuNNote2TKFbBFLOjvD0qEtqBqQcYV6aQmN2JQsZbRTNTSpkXbPEsZxLhzEFScaNe_UnpHEpYHl0qBYfcaFTBQXrA"
host = "https://advertising-api.amazon.com"
result = get_keyword_recommendations(asins, access_token, client_id, profile_id, host)
print(json.dumps(result, indent=2))

if 'error' in result:
    print(result['error'])
else:
    # 保存结果到 Excel 文件
    save_to_excel(result, '修脸器-v3-点击量.xlsx')
#     # save_to_excel(result, '阻力带-v3-转化率.xlsx')
