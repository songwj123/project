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

    try:
        response = requests.post(url=url, headers=headers, json=request_payload)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}


asins = [
    'B0BHRZBHNX'
]
profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIPxpbmxl1FKhRjOu4j9W7rguGfGyfOJ1fZIgfu5lCKzDwOxhlGczkUCF6PUvBoLai-oadD0St_qg799wJro8C3Mz0Pktn58YAFBOAMER8tbv4SrI8fMXhfHHAbbeFFFfXj2RQZJjhAYhU1_9n6-RzLPO6XYdltEQ-zKMfaMso3Y6gzB2dbUjCBOTR3OtGGJOy7jQU2Wnekj0U-ZA7UZxdrliqSe5WkE7L_aaSM6VRAgyx7R-IU5KMk4LXOtm6fJf-94PaOMtwaSZQWhwC45xy2n4PlswQiL0drKguNYUuUITT_C79zcSsXP0FN5Agt7A3CveaRnCpBpFA81yu2X0Mjn89e_8Ysz2_DnPqul-5blsZDfgNW3X0as-8dxq_vNQSzPJOTAkhcgy7ktmoUtHl4LG7fplllGOPmjX0ku6ZUKWegY8s2lHvitBGgHnRctovh1qr_izN4P0jRyzCRsyzCtg"
host = "https://advertising-api.amazon.com"
try:
    result = get_keyword_recommendations(asins, access_token, client_id, profile_id)
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f'Error: {e}')
