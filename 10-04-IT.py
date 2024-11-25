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
        "locale": "it_IT",
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
        "locale": "it_IT"
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
    # keyword2 = get_keyword_recommendations_v2(api, access_token, client_id, profile_id, asins)
    # keyword3 = get_keyword_recommendations_v3(api, access_token, client_id, profile_id, asins)
    similar_asins = get_asins(api, access_token, client_id, profile_id, asins)

    decoded_data = {
        "title": decode_unicode(title),
        "description": decode_unicode(description),
        # "keywords_v2": decode_unicode(keyword2),
        # "keywords_v3": decode_unicode(keyword3)
    }

    url = "http://118.31.220.183:8003/keywords_retrival"
    # url = "http://120.27.213.121/keywords_retrival"
    payload = {
        "taskid": "4157-s5a93-9034",
        "asin": str(asins[0]),
        "subject": subject,
        "title": decoded_data["title"],
        "country_code": country,
        "similar_asins": similar_asins,
        "description": decoded_data["description"],
        "keywords": {
            "v2": [],
            "v3": []
        }
    }

    response = requests.post(url, json=payload)
    print(json.dumps(payload, indent=4))
    # print(f"请求状态码：{response.status_code}")
    return response.json()




profile_id = "1322367844724023"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIMmg0qZxmywlpjMGGjFBUlumddrIAFgz2qha7rlQp1A_-uZPs2xMYG_UPDU--_w0LvfSAm1jhD2qAg_z8biWIyWehZY_5g8AMv9Lj2Z-rnkscHMU4QoSX43tyVfzVnUcyFfnaLUIEM9edTbFEg-pLgyCUxzIlx2HN5j84OFvUBwohGzp032IVc5ipgLuEpRi6X8M_ygwR8pcXLeID8fNhlzzRAPr4J8TFFV-YdB2TjyuiIeSjXXnflijAFodHtuzuPc1axIZFGc5fyaZ7N2nDSnNcygT38sfYP9DKVImZJjMpYAFJdIA7hF7Ieu3zduhZIkEZ64SY9vadq5ZT5Cv7nwEe4YTeHkK58qTg6NJv8YHczC8cgSenW1ekaTgs-THR_UpOdYB3xgBepPpJ8GvslR1k_F1lnbOZTzktjlBIx-hBd1C3ffubtG0NJTXOe2IPatJHULF33KxfpWzGkgN-J6FL6r_zqcYkPDk0o7dIaMO-79uleJIZwqVnmTHxhgd4U47i_bs4fnU1xZHhCA34wG3"
asins = [
    "B0B5DLQ69R"
]
api = "https://advertising-api-eu.amazon.com"
country = "IT"
subject = "Sacco nanna invernale per bambini"
title = "Mosebears Sacco nanna invernale per bambini, 2,5 tog, 100% cotone, per diverse misure, dalla nascita all'età di 24 mesi (animal, 12-18 mesi)"
description = """
100% cotone di alta qualità, mantiene caldi: il sacco nanna neonato è dotato di un’imbottitura calda, è senza maniche, di alta qualità, sicuro e sano per il vostro bambino. Il sacco nanna mantiene una temperatura costante.
Disponibile in quattro diverse taglie: si consiglia di scegliere la taglia giusta in base all'altezza del bambino. taglia S: da 0 a 6 mesi, taglia M: da 6 a 12 mesi, taglia L: da 12 a 18 mesi, taglia XL: da 18 a 24 mesi.
Eccellente design con cerniera: la cerniera è priva di nichel per prevenire le allergie. Il design con bottoni e il colletto evitano graffi sul mento e sono molto facili da indossare e da togliere.
Universale, adatto per tutto l'anno: Il nostro sacco nanna neonati da 2,5 tog è super morbido, confortevole, offre un ottimo sonno, adatto per temperature ambiente inferiori a 20 ℃, dotato di design senza maniche. In questo modo può essere utilizzato in tutte e 4 le stagioni.
FACILE MANUTENZIONE: il nostro sacco nanna per bambini è lavabile in lavatrice fino a 30ºC e può essere asciugato a bassa temperatura, può essere lavato più volte, è resistente e mantiene molto bene la sua forma.

"""
result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description,
                                         country)
print(result)

'''
ES/FR/GB/DE/US
'''
