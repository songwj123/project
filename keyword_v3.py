import requests
import json
import pandas as pd


def get_keyword_recommendations(asins, access_token, client_id, profile_id):
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,  # 最大推荐数量
        "sortDimension": "CLICKS",  # 排序维度，使用 {“CONVERSIONS", "CLICKS"} 进行排序
        "locale": "en_US",  # 语言设置
        "biddingStrategy": "AUTO_FOR_SALES",  # 出价策略
        "bidsEnabled": True,  # 是否启用出价建议
    }

    url = f"https://advertising-api.amazon.com/sp/targets/keywords/recommendations"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v3+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v3+json'
    }
    response = requests.post(url=url, headers=headers, json=request_payload)
    response.raise_for_status()
    return response.json()


asins = [
    'B0BHRZBHNX'
]
profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIBVpngKK71EYVI66gWk2HomBy1C7cBHIZyikVXME-1zKBbngvmbljTJ9VEYlBXY-t44E_wb8Et-jTL7C4DQ8l7KryujO0hhBx3lvWxg3PlUyC0aEA2M4HMBSEKO8ORqaGp3zhQycZyW4n0L-9vloZWDsKD1ZLedDb6dyh4q8j8ZlYUAOMm1ywTCx8nPz7IWo_7xLolFUP11uaTErgKGw59mplHKUZ1FgBP5oyLMYofus4lVpFXFgYJg--zyBf-MUzpNCDLQ6l-89LeD1UXlepEsZH6FqqIWy4bO3Pu6dz9KqkRrXuM_LlxdL9yNw-B2JW8DaZkvvkEc9UrUwVnfgDJcCQwSHypO1s7Zufw5LJBJZLn-9-B3i_ORVshGgtGHezgEBCe1nUjCVnKp5yo0VRrZbiWA5huarC7E1kLRhmW3kStH1ubioMeqUVX2X6ub1hBaatCvHpWVhLwpvv-WWWhWMFbMNqIcaiw1gXpWOZrJwFA"

try:
    result = get_keyword_recommendations(asins, access_token, client_id, profile_id)
    res_list = []

    for r in result:
        res_list.append(r['keyword'])
    print(res_list)
except Exception as e:
    print(f'Error: {e}')
