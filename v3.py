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
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v3+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v3+json'
    }
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,
        "sortDimension": "CLICKS",
        "locale": "en_US",
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
        "locale": "en_US"
    }
    res = requests.post(url, headers=headers, json=data)
    if res.status_code == 200:
        response_json = res.json()
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {res.status_code} - {res.text}")
        return None


def send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description):
    keyword2 = get_keyword_recommendations_v2(api, access_token, client_id, profile_id, asins)
    keyword3 = get_keyword_recommendations_v3(api, access_token, client_id, profile_id, asins)
    similar_asins = get_asins(api, access_token, client_id, profile_id, asins)

    decoded_data = {
        "title": decode_unicode(title),
        "description": decode_unicode(description),
        "keywords_v2": decode_unicode(keyword2),
        "keywords_v3": decode_unicode(keyword3)
    }

    url = "http://120.27.208.224:8003/keywords_retrival3"
    payload = {
        "asin": str(asins[0]),
        "subject": subject,
        "title": decoded_data["title"],
        # "country_code": country,
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


profile_id = "2651906346803655"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIBDGb7TqKVyjYFxVz6Jz3Dyvz9kd3j_zR1eFtyUE4tUfP6BPZHt-CKqh5isgn9Knrk8IhtrK913c1zN9qE1vIMXIa3mjXT-dwQgyE1nlnuVfxSkZGPiICYee1oKGJuFUlJlzCTkvhCnmqzws2GVuPZUEm2Hd1b5LuGYHySfgK5W3u6jiiA1VYi_b7IcXyNfmbVTm4f3jDgYi-uzX6oeEyi0a8jSMfyaI8xyvXGSZkOI3syuda4KArnbqLu5qU9bu9vhp_bY8uereH7879wy9o6rJoHm-6sg_BpzsEdA3iursg9a2YWc3vxA6OUU9BcJKLJFP4E-FgRPxGjBMQXPLMtSOKlCLJJjpW4hAdMfAGrg96giwTdJ_UmhJ1h8IDKK8Op6CdUoPAHtbe_ZN8ROPlaUmaYbrpKK3Csi56k25REezx0RznTnCzPH0ChT_UZaxW8ull9EfnKWiOse-RhyYoS4C"
asins = ['B0D8Q15LPC']
api = "https://advertising-api.amazon.com"
# country = "GB"
subject = "Facial Hair Remover for Women"
title = "Facial Hair Remover for Women, Face Hair Trimmer, Rechargeable Women's Facial Shaver, Painless Lady Shavers for Women for Face Hair, Upper Lips, Peach Fuzz, Bikini Body-White"

description = """Facial Hair Remover for Women: The facial epilator can quickly and gently remove facial hair, including upper lip hair, peach fuzz, and more. Smooth, painless, precise hair removal, smoothing skin and preventing skin damage.
Easy to clean: The facial epilator is very easy to clean, just unscrew the blade part, clean the hair with a cleaning brush, and rinse directly with water.
USB Rechargeable: This facial epilator is equipped with USB charging function, eliminating the trouble of frequent battery replacement, convenient and environmentally friendly.
Compact and Portable: The mini and portable design makes it easy to carry in your purse or travel bag. Whether you're at home or on the go, maintain a flawless look with this compact hair removal device.
Built-in LED Light: Enhance visibility during use with the built-in LED light feature. Illuminate the treatment area for precise and thorough hair removal, ensuring you achieve the desired results with ease.
⚠️Please note: We offer 30 days returns and 7*24 hours customer service. If you have any problems during use, please feel free to contact us and we will provide you with timely and efficient after-sales service.
"""
result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description)
print(result)
'''
ES/FR/GB/DE
'''
