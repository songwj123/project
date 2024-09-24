﻿import pandas as pd
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
        "locale": "es_ES",
        "biddingStrategy": "AUTO_FOR_SALES",
        "bidsEnabled": True,
    }
    response = requests.post(url, headers=headers, json=request_payload)
    response.raise_for_status()
    results = response.json()
    if response.status_code == 200:
        # return json.dumps(results, indent=4)
        res_list = []

        for r in results["keywordTargetList"]:
            res_list.append(r['keyword'])
        return res_list
    else:
        response.raise_for_status()


def get_asins(api, access_token, client_id, profile_id, asins):
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
        "locale": "es_ES"
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

    url = "http://120.27.208.224:8003/keywords_retrival4"
    payload = {
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
    return response.json()


profile_id = "2223225971933875"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIPDwQ3THzaFOWduvcoIyvlsLTHW9EbzLecWZuKjlfiPbT2LFAWzf3NVne-TPwlx9WjucplAvP5CO1_-WHCgOn8WFZWD0y9RiHzH2yZYTlQMNsNKq1PfyO2RpxCHHrpVTucE8q9_BItonRkkJ2JvdcPU8crnmuzgN6lnaTb2iwGh9cOPJVN4o0N7NuMIGsnQybr9DBoTExCDJRJyFYA-1M_n-n1lAY1wWBjzfJfmf7YzyNrr0Sm8_-BdxP5_-PbVF6nVpRWF0NO9YoQSCgEAKU_2ZJjpl9K4o41a8JYRSqfTMcFwB2tEjEz_JocQqvC97nv4JmVH0VavaWA6XRiHYMzB2E9puF0qod3wtC3x7X5_XhYNIMq73Mp_hNKRH7IefIS8dwqDtUdlr1ltx6XzbVxAICDdOw0NlbDQzCOzRJccQm8uO7De8Fi5Bsl2EgWgFbD8sLqELez27ADeUeklViTKtFqyHdO7hdGnq4AuGVf_EHA"

asins = [
    "B0D9YBRZL4"
]
api = "https://advertising-api-eu.amazon.com"
country = "GB"
subject = "LED Flash-White"
title = "elestyle Wireless Doorbell with 2 Receivers, 150M Long Range Door Bells Battery Operated, Door Chime kit with 60 Melodies, 4 Volume Levels, LED Flash-White"
description = """Dual Receiver Design: The wireless doorbell comes with two receivers, perfect for larger homes, ensuring you hear the doorbell clearly from any corner of your house.
60 Melodies to Choose From: With 60 different chimes built-in, you can easily customize your doorbell sound to match your personal preferences.
Adjustable Volume with 4 Levels: The doorbell features four adjustable volume levels, allowing you to set the perfect sound level for your environment, ensuring you never miss a visitor.
Long Wireless Range up to 150m: With a wireless transmission range of up to 150 meters, the doorbell maintains a strong connection even in multi-story buildings, free from distance limitations.
Easy Installation and Durable: Designed for convenience, this wireless doorbell is easy to install and built to last, requiring minimal maintenance, making it an ideal choice for home security.
"""
result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description,
                                         country)
print(result)
'''
ES/FR/GB/DE
'''
