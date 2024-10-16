import requests
import json
import pandas as pd


def get_keyword_recommendations(asins, access_token, client_id, profile_id):
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 100,  # 最大推荐数量
        "sortDimension": "CLICKS",  # 排序维度，使用 {“CONVERSIONS", "CLICKS"} 进行排序
        "locale": "en_GB",  # 语言设置
        "biddingStrategy": "AUTO_FOR_SALES",  # 出价策略
        "bidsEnabled": True,  # 是否启用出价建议
    }
    url = f"https://advertising-api.amazon.com/sp/targets/keywords/recommendations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v5+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v5+json'
    }
    response = requests.post(url=url, headers=headers, json=request_payload)
    response.raise_for_status()
    return response.json()


asins = [
    'B0D5TR7BF9'
]
profile_id = "2651906346803655"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBINnql-ktVkvXFdPJHaxsxnSrq6YaGS2XR4gg6VW8dPXE5JssOBClFZ1cR7JQk7by8GPLnktgRW_kIGguRr0btFukEXY0CxZbHyg5g6hntxjvmsS9FJfBLBbbpWHVtAqpF8RRHgPX-3Azd3yBUMAuASjGyWOJ-k5R8GkNBMJ--4N0tK8Jl_N8GvB4Lz2CUmucMwhbWpUYAgNFO3eFDA3RGieRK6isa0P4YEpBdPWWkxcCejEPYX1yxO_O6kd29-Qg8P5XHDSm056j1GhxQwdiatQ9wB_uyozLrZCITG3P7GmDmqG9fXZg8-0Ab3ybkf4uJMACuD1ZoPaJnWUj89x_n2DDo5UZK7XeZwYb2KTGtLjta73FyZ1c1IT_hE6n-uJsFzOBplm3_1khn6ovPscAI8agLeM1MtzkafmBr6BvO1w2SNLocn6kt5ZiRFMzmjK6ozS9hb4auz9FOvB6wD1yC5cSnW_2JGDHPqLlYs9qp-UTMQ"

try:
    result = get_keyword_recommendations(asins, access_token, client_id, profile_id)
    # print(result)
    res_list = []

    for r in result["keywordTargetList"]:
        res_list.append(r['keyword'])
    print(json.dumps(res_list, indent=4))
except Exception as e:
    print(f'Error: {e}')
'''


'''