from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests
import json
import ast


def decode_unicode(input_data):
    """解码输入中的 Unicode 转义字符"""
    if isinstance(input_data, str):
        try:
            return ast.literal_eval(f"u{input_data.encode('unicode_escape').decode('ascii')}")
        except (ValueError, SyntaxError):
            return input_data
    elif isinstance(input_data, list):
        return [decode_unicode(item) for item in input_data]
    return input_data


def get_keyword_recommendations_v2(api, access_token, client_id, profile_id, asins):
    url = F"{api}/v2/sp/asins/suggested/keywords"
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


def get_keyword_recommendations_v3(api, access_token, client_id, profile_id, asins):
    url = f"{api}/sp/targets/keywords/recommendations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v5+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v5+json'
    }
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,
        "sortDimension": "CLICKS",
        "locale": "en_CA",
        "biddingStrategy": "AUTO_FOR_SALES",
        "bidsEnabled": True,
    }
    response = requests.post(url, headers=headers, json=request_payload)
    response.raise_for_status()
    results = response.json()
    if response.status_code == 200:
        res_list = []

        for r in results["keywordTargetList"]:
            res_list.append(r['keyword'])
        return res_list
    else:
        response.raise_for_status()


def get_asins(api, access_token, client_id, profile_id, asins):ss
    url = f"{api}/sp/targets/products/recommendations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spproductrecommendation.v3+json',
        'Accept': 'application/vnd.spproductrecommendation.v3+json'
    }
    data = {
        "adAsins": asins,
        "count": 47,
        "locale": "en_CA"
    }
    res = requests.post(url, headers=headers, json=data)
    if res.status_code == 200:
        response_json = res.json()
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {res.status_code} - {res.text}")
        return None


def send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description,
                                    country):
    keyword2 = get_keyword_recommendations_v2(api, access_token, client_id, profile_id, asins)
    keyword3 = get_keyword_recommendations_v3(api, access_token, client_id, profile_id, asins)
    similar_asins = get_asins(api, access_token, client_id, profile_id, asins)

    decoded_data = {
        "title": decode_unicode(title),
        "description": decode_unicode(description),
        "keywords_v2": decode_unicode(keyword2),
        "keywords_v3": decode_unicode(keyword3)
    }

    url = "http://118.31.220.183:8003/keywords_retrival2"
    # url = "http://120.27.213.121/keywords_retrival"
    payload = {
        "taskid": "61981sa8",
        "asin": str(asins[0]),
        "subject": subject,
        "title": decoded_data["title"],
        "country_code": country,
        "similar_asins": similar_asins,
        "description": decoded_data["description"],
        "keywords": {
            "v2": decoded_data["keywords_v2"],
            "v3": decoded_data["keywords_v3"]
        }
    }

    response = requests.post(url, json=payload)
    print(json.dumps(payload, indent=4))
    # print(f"请求状态码：{response.status_code}")
    return response.json()




profile_id = "3218265756783695"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBILV7F3pAdchtUsxa0coYPjUqq0NjpWxgqKknyWPaVLqka2BvqKu8lgBHkfDocBaPj4o1OdcfgTuO4Q2NxTMs2T8Avb1n-t0ywEfUCg4gnUbeGGCdpkPlD0ltKulqY6qpZujU_Gzn36HxQQm9y11y32F5w0Dbcl5jx_XNswvDHpIdrAeqjfo6sHWXJXR5PPMWDTSGH7UsPSjphg8Ic61oC-Vb8_A1ujyMW1ZOoEAmeKplEvFQJaeY61VkWV_pO2pQQje6Wc9W7DE4q7bESKW1R1YX_gpEBWI7KnsXoj_NUG7KAYawQex1i_x0cg1PM6CMwIXK01bV2M9yntNW1KZ37xxljSdN01a7EDGyeFlKQEqPAWANLeewFoiTAq1qqqpBANqEl3w8Qh46ZcpyRTxFXysDSs7Kro3n9pVaAGArLOz8KO5bgCZQ-QLXNVEXgr2wC3B_sjehUt_wsTcBX1tA4M7Gk5ZAtoq-2gHFR2KiwN34oHpdSpAIP1MkfefPH2xE6mAPXVqQo2it8RHLXO1_zPOW896aXMYVvCkygTgTPA92IQ"
asins = [
    "B0B6TYPNF6"
]
api = "https://advertising-api.amazon.com"
country = "CA"
subject = "Facial Hair Removal for Women"
title = "KRADAA Facial Hair Removal for Women: Rechargeable Hair Removal Device - Painless Womens Face Razor Peach Fuzz"
description = """
Painless Hair Removal: Effortlessly removes facial hair from lips, chin, and cheeks without irritation or discomfort.
USB Rechargeable: Convenient and eco-friendly, featuring a USB rechargeable battery for long-lasting use.
Compact & Portable: Lightweight and travel-friendly design, perfect for quick touch-ups on the go.
Replacement Heads Included: Comes with 2 additional replacement heads, ensuring extended use and cost savings.
Safe for All Skin Types: Gentle and effective, designed to be safe for every skin type, providing a smooth finish.
"""
result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description,
                                         country)
print(result)

'''
ES/FR/GB/DE/US
'''
