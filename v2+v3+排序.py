import pandas as pd
import requests
import json
from openpyxl import Workbook


def get_keyword_recommendations_v2(access_token, client_id, profile_id, asins):
    url = "https://advertising-api.amazon.com/v2/sp/asins/suggested/keywords"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Amazon-Advertising-API-ClientId": client_id,
        "Amazon-Advertising-API-Scope": profile_id,
        "Content-Type": "application/json"
    }
    payload = {"asins": asins, "maxNumSuggestions": 1000}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            keywords = [item.get('keywordText', '') for item in data if isinstance(item, dict)]

            return keywords
        else:
            raise ValueError("Unexpected response format: Expected a list")
    else:
        response.raise_for_status()


def get_keyword_recommendations_v3(asins, access_token, client_id, profile_id):
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,
        "sortDimension": "CLICKS",
        "locale": "en_US",
        "biddingStrategy": "AUTO_FOR_SALES",
        "bidsEnabled": True,
    }
    url = "https://advertising-api.amazon.com/sp/targets/keywords/recommendations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v3+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v3+json'
    }
    response = requests.post(url, headers=headers, json=request_payload)
    response.raise_for_status()
    results = response.json()
    if response.status_code == 200:
        res_list = []
        for r in results:
            res_list.append(r["keyword"])
        return res_list


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
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def send_keywords_retrieval_request(access_token, client_id, profile_id, asins, subject, title, description, count):
    keyword2 = get_keyword_recommendations_v2(access_token, client_id, profile_id, asins)
    keyword3 = get_keyword_recommendations_v3(asins, access_token, client_id, profile_id)
    similar_asins = get_asins(access_token, client_id, profile_id, asins, count)

    url = "http://120.27.208.224:8003/keywords_retrival3"
    payload = {
        "asin": str(asins[0]),
        "subject": subject,
        "title": title,
        "similar_asins": similar_asins,
        "description": description,
        "keywords": {
            "v2": list(keyword2),
            "v3": list(keyword3)
        }
    }

    response = requests.post(url, json=payload)
    print(json.dumps(payload, indent=4))
    return response.json()


# def save_keywords_to_excel(result, asins):
#     # 根据传入的 ASIN 列表生成文件名
#     file_name = f"{''.join(asins)}.xlsx"
#
#     data = {
#         "Bid Words": result.get('keywords', {}).get('v2', []),
#         "CR Words": result.get('keywords', {}).get('v3', []),
#         "Broader Words": result.get('broader_words', []),
#         "Negative Words": result.get('negative_words', [])
#     }
#
#     with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
#         for sheet_name, keywords in data.items():
#             df = pd.DataFrame(keywords, columns=[sheet_name])
#             # 将每个 DataFrame 写入不同的工作表
#             df.to_excel(writer, sheet_name=sheet_name, index=False)


profile_id = "2235613932456084"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIOfUFlFcWcBzlfs09ukA6BB2Vg5Tb0Wnor4Rsdr81OgrOy9vuNj3bd67bi5AEKTqk5SVy4Qra5nZ70xsV7FCXUJbfPDlfeLqHWSquSOEm_7tDdhLSlvPkudyW1my7HyiyC19MaPSHQEli7sQ-lg2OhWAd2zxOc7slk1gfLBTz1oUwfSFqt_jzW9_y72VaDakcKSkyMupOwV-8ldnSM16OBrV47M9Q9gC6oxyhr7agJU3261A_1M_OXSJ7ZY7PliZ73ScTbLWd-FrPSdwj4GtDfDxKbTRuT00L09gA5pBtcDE-KlgnHI0iUmmQKNtyRK4VKti5DHtVicnK_LvImJV811iri6z-MOARlTjrZx1BQI6NkAjD1o6Tc2RBiEkj2disWcharM7IkxNSuH3lkrFSP6kRUz2B2Nx7I_QvcThN3brCE_Xk2ySBMaIIBWfnvzSN06vzT7KfunntiZb1gJO63iE"
asins = [
    "B08TV7KP8V"
]
count = 47
subject = "Grow Light for Indoor Plants"
title = "LED Grow Light Indoor Plants - 300W 420LED Plant Light with 63 Extendable Tripod Stand,Dual Controllers,Full Spectrum,4/8/12H Timer,Adjustable Gooseneck,4 Switch Modes for Greenhouse Veg and Flower"
description = "【2021 New Upgrade & LOWER RUNNING COSTS & HIGHER-QUALITY YIELDS】: LECLSTAR Grow light for indoor plants, Four-Head three-row designs, the whole lamp is composed of 420 LED high-brightness lamp beads. It only needs 40W of power to transmit 300W, high efficiency, and energy-saving, LECLSTAR Grow light can increase the growth rate of indoor plants by 50% compared to other grow lights.Meanwhile our high-quality aluminum shell are great at heat radiation with a lamp life of up to 50,000 hours.【Dual control, automatic on/off】 LECLSTAR Grow light with line-in controller and RF controller. Plant light Support 3 light modes, 10 dimmable levels, 4 lights independent control, and auto on/off every day after setting the 4H/8H/12H timer,so there is no need to worry about plant withering when nobody at home.every feature is comendable. UL certified adapter with USB plug, more safe and flexible to use in anywhere with the grow light【Adjustable height, easy to install】 Just within two minutes! Open the tripod, adjust height（Adjustable tripod stand extendable from 11 inches to 75 inches, just lock it at desired length for your preferred use.）, turn the screw clockwise until it’s secured, place the grow light on the tripod, turn the screw counterclockwise until the plant light is fully seated.Grow light Suitable for indoor plants, greenhouse, darkroom, living room, office large and tall plants, flower show, potted plants.【Full Spectrum grow light & larger lighting area】1.Red(660nm)+Blue(460nm): promote plant growth, flowering and fruit. 2.Warm White:3000k high uniform light, like sunlight,improve seeding growth. 3.Red+Blue+Warm White(380nm-780nm):Enhance red and bluelight based on natural light,effectively promote growth.Besides,the 4-head grow light has a 360-degree flexible gooseneck made from high quality tubing to adjust an ideal illumination angle and Provides a larger light exposure range for your plants"

result = send_keywords_retrieval_request(access_token, client_id, profile_id, asins, subject, title, description, count)
print(result)
