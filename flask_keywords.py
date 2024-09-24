import pandas as pd
import requests
import json
import ast
from flask import Flask, request, jsonify

app = Flask(__name__)


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
    url = f"{api}/v2/sp/asins/suggested/keywords"
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
        res_list = [r['keyword'] for r in results["keywordTargetList"]]
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


def save_keywords_to_excel(result, asins):
    bigwords = result['data'].get('bigwords', [])
    crwords = result['data'].get('crwords', [])
    broader_words = result['data'].get('broader_words', [])
    negative_words = result['data'].get('negative_words', [])
    crwords_rank = result['data'].get('crwords_rank', {})

    def get_rank_data(words, rank_data):
        data = []
        for word in words:
            rank_info = rank_data.get(word, {})
            src = ', '.join(rank_info.get('src', [])) if rank_info.get('src') else ' '
            rank = rank_info.get('rank', None)
            data.append({'高转化词': word, '来源': src, '排名': rank})
        return data

    bigwords_data = [{'大词': word, '来源': ' ', '排名': rank} for word, rank in
                     zip(bigwords, result['data'].get('bigwords_rank', [None]))]
    crwords_data = get_rank_data(crwords, crwords_rank)

    data = {
        "大词": bigwords_data,
        "高转化词": crwords_data,
        "广泛词": [{'广泛词': word} for word in broader_words],
        "否定词": [{'否定词': word} for word in negative_words]
    }

    with pd.ExcelWriter(f"{asins[0]}.xlsx", engine='openpyxl') as writer:
        for sheet_name, keywords in data.items():
            df = pd.DataFrame(keywords)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"数据已成功保存到{asins[0]}.xlsx")


@app.route('/retrieve_keywords', methods=['POST'])
def retrieve_keywords():
    data = request.json
    asins = data.get('asins')
    country = data.get('country')
    subject = data.get('subject')
    title = data.get('title')
    description = data.get('description')
    profile_id = "2223225971933875"
    client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
    access_token = "<YOUR_ACCESS_TOKEN>"
    api = "https://advertising-api-eu.amazon.com"

    result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title,
                                             description, country)

    save_keywords_to_excel(result, asins)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
