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
    url = f"https://advertising-api-eu.amazon.com/sp/targets/keywords/recommendations"
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
    'B0CL5FGK4V'
]
profile_id = "2223225971933875"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = ("Atza|IwEBINNimtp_S91FY2UROAB-fgxpXH5nA-wGKq1CCQQjABREFKz4Izk1cJMP8pUZIuAGGmf8S1EXGI360k1iBrZHnUx9Vu24AlSpeuwu8EpKNa5e_CZAqinGHFKCbQM-vOCmliwlctSh41pOWPvM7urwA6WFs9Vr1I4xWS5DZOBwOOhOf30HD49cbVd2buPIV2i2YlpAqGrDrSrf-bu1_RE6kTqGVG2es58DGdZ65sGVhNqBg9qFjo95TEcu1NOx0IJmD0BuiBXKP-oGM4rLkYBJysrW4LtEYpQ_4uI29RigXHPR6_XtTzBvo3Itp0stqI22Ivlu8XOcQdk6hswNIgIUjz1cbxa4vbeL64hbTyeorfc6Sxo6rVGohXAOsh9--HT-m_d11QbDaCXSnjxTD4i_Aag-NVOFPgHQvxo3yf4DG2yzKD1YB1DBPdoHMaICKfg_s8MUO_FspngbKWej8eXdBRTV")

try:
    result = get_keyword_recommendations(asins, access_token, client_id, profile_id)
    # print(result)
    res_list = []

    for r in result["keywordTargetList"]:
        res_list.append(r['keyword'])
    print(res_list)
except Exception as e:
    print(f'Error: {e}')