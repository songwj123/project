import pandas as pd
import requests
import json
import ast
from concurrent.futures import ThreadPoolExecutor, as_completed


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
        "locale": "en_GB",
        "biddingStrategy": "AUTO_FOR_SALES",
        "bidsEnabled": True,
    }
    response = requests.post(url, headers=headers, json=request_payload)
    response.raise_for_status()
    results = response.json()
    if response.status_code == 200:
        res_list = [r['keyword'] for r in results.get("keywordTargetList", [])]
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
        "locale": "en_GB"
    }
    res = requests.post(url, headers=headers, json=data)
    if res.status_code == 200:
        response_json = res.json()
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {res.status_code} - {res.text}")
        return None


def send_keywords_retrieval_request(api, access_token, client_id, profile_id, asin, title, description, subject, country):
    keyword2 = get_keyword_recommendations_v2(api, access_token, client_id, profile_id, [asin])
    keyword3 = get_keyword_recommendations_v3(api, access_token, client_id, profile_id, [asin])
    similar_asins = get_asins(api, access_token, client_id, profile_id, [asin])

    decoded_data = {
        "title": decode_unicode(title),
        "description": decode_unicode(description),
        "keywords_v2": decode_unicode(keyword2),
        "keywords_v3": decode_unicode(keyword3)
    }

    url = "http://118.31.220.183:8003/keywords_retrival"
    payload = {
        "taskid": "61981sa8",
        "asin": asin,
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
    return response.json()


def process_excel(input_file, output_file, api, access_token, client_id, profile_id, country):
    df = pd.read_excel(input_file)
    results = []

    def process_row(row):
        asin = row['asin']
        title = row['title']
        description = row['description']
        subject = f"Product: {title}"

        try:
            result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asin, title, description, subject, country)
            row['similar_asins'] = json.dumps(result.get('similar_asins', []))
            row['keywords_v2'] = json.dumps(result.get('keywords', {}).get('v2', []))
            row['keywords_v3'] = json.dumps(result.get('keywords', {}).get('v3', []))
        except Exception as e:
            row['error'] = str(e)
        return row

    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_row = {executor.submit(process_row, row): row for _, row in df.iterrows()}
        for future in as_completed(future_to_row):
            results.append(future.result())

    output_df = pd.DataFrame(results)
    output_df.to_excel(output_file, index=False)


# 使用示例
input_file = 'input.xlsx'  # 包含 asin, title, description 列的 Excel 文件
output_file = 'output.xlsx'  # 输出结果保存的 Excel 文件

api = "https://advertising-api-eu.amazon.com"
profile_id = "2223225971933875"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIN1nF-dK2PtMRwD6zdEXef1FT1alJso2yCIcH4Mi15dYzNbJu4mlwLTNYFYMkonllPk1Api1e1oSlGorUwcAwbQ-JT-fUsrbVHmkRb7RXh0-hHXG64Xjyk8Eb-wBYErcRc-kC8v2eaxCcvc0u00Z_HNwWCcEeFiAd_0Yj095croyhriQ88mSRfU2oV3Wy_b7tOKyxW-Gf8QeKMrxupIwiKdkc2vjvzMmB8272SwzrdSWVkIOUdt2ax4HNiiYVCc18vnGfMK7-UkGeB7ggLyQmy4gvCXEhQn2ul0v8fF7mwJzrhRu7Bv7JI-tPjoABnkmrPCUXFWwwdzalqnyaaN4S1FIfHS-XNPOSzIH_NK7At8gzL8-CT0bC877xFdJ6UbBKT8UT6hgm23VxJuiGZgY4lisrhdhX2Dr3CWMK6SBvWZeP2eDS7PXkq_e6AyJJI7q2XPmPMUDiB1nEiLa6fTbNnrp-TI__HlcfeXQ5GDYffC2nA"
country = "GB"

process_excel(input_file, output_file, api, access_token, client_id, profile_id, country)
