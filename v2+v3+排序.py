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

    url = "http://120.27.208.224:8003/keywords_retrival"
    payload = {
        "asin": str(asins),
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


profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIH2seQO12o9-WI8iql3yErJOv5DkgX3F1OXFqUJ1Zj5zQCv8xk6UMoUUMhYMD_TlPli28JHHpX6LgQwD4iJaCOW72Nkid7mWLC7b3WG0rmKqstHxcUWCTZUpgyTgGaEtWi4H5_WDmG_aUjqMyuAq0GLY_3WvbA-8iboHXUY5t17kt3gdmNmw3rBfVT4qgyQscwmkZ_TVszAlco3mCZ_tdW2Is3jncHmOT3FJSEqyoBJz7G64b-zjMlTjTzcKGQa2NbreamjciPv31XNUnUKEkn0phGYJKSso19FYAIqFesX6_rZ2iOQAaG_7E8fvr0O_j3lQXU5F16Aq0tX9EReG_SNpX83cd9ueVl_U3j6S8B1ck-57ZY83mNwK_RdlPvHMuUDbWWnXya-0MeaOtIIbjlLYrox5PIihvB4yMlHgy1nkv6Ndk4FdeDW5hmntvOvkldDaMcqQCgX4mBnGnBXiz5Y-"
# asins = [
#     "B0D6G2ZCJS"
# ]
# count = 47
# subject = ""
# title = "Electric Foot Callus Remover, 16 in 1 Rechargeable Pedicure Kit, Waterproof Scrubber Dead Skin Removal Tool with 3 Rollers & 2 Speeds for Feet Care, Battery Display - Black"
# description = "16 in 1 professional pedicure kit : The electric feet callus remover is made of high-quality material, with electronic pedicure tool included cuticle remover, fine file, 2-sided foot file, cuticle fork, callus scraper, sandpaper file etc. This is a complete foot care kit that can meet your different needs without the need to buy additional accessories.2 Speeds Adjustable & 3 Roller Heads : This foot sander comes with 3 different quartz scrub heads and featuring two speeds. The low speed is 1600 rpm for hand calluses and delicate skin care; the high speed is 1970 rpm for stubborn calluses and dead skin. Easy to operate, you can adjust the speed on demand, convenient and practical.Fast charging & Long Lasting: Electric callus remover for feet built-in rechargeable 1200mah battery, the battery life is long-lasting, so you don't have to worry about running out of power in the middle of using. Equipped with a usb fast charger that allows you to fully charge in about 2.5 hours, and the battery level can be displayed.IPX7 Waterproof & Light: With high level IPX7 Waterproof for wet and dry use, the foot pedicure kit whole body can be rinsed under running water, so it’s convenient to clean and use. Equipped with light that can help you see more clearly when cleaning dead skin.An Ideal Gift & Friendly Service: Our electric foot file is perfect for everyday use or holidays as gifts for your family, friends. If you encounter any problems when using this foot grinder , you can contact us, we will provide a friendly after-sales service."
asins = input("请输入ASIN：")
count = input("请输入推荐数量：")
subject = input("请输入主题：")
title = input("请输入标题：")
description = input("请输入描述：")



result = send_keywords_retrieval_request(access_token, client_id, profile_id, asins, subject, title, description, count)
print(result)
