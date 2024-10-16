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
        "locale": "en_GB",
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

    # response = requests.post(url, json=payload)
    print(json.dumps(payload, indent=4))
    # return response.json()


profile_id = "1724874051069213"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIOwvaDIdq7EAbwdu5wh4pwmAMZq7jB4J4EHLK2AO7cOtEHKEk3XbjKNiffwV8F7Hvasd1XeJMggcIC5ldPWIfZ25EdtVTkmt6q8T4qzYbQgQ-_yGCD8FeHA6vYTZV35w9wRzO6LLXsnIPWYUwpL4Jli44h70RaGH3OHCOuwraB90xMTuDhamVTRMIHC0zA_mqCtYZfMbSzTrHU1nJM50bX2tWlgnQ8vqIELA6hl35ZxoxCxYQKBVud9dTLDDoiay_XfR18kbkDuB9wzHp6W5IkP2m0DfKYEcInn8PrnEz1rFcx_TisJ-Nr---e0zEyqT6omZ-AcLgq-yrrafB8p1SpiXOHOCgRXPJ2_yWcJzw8KIPK7KJq2ZWf3EpwJ6gn_IwK6H99fUWOLaiEg-rUkMlyboPhlrCH2higVcP3RiMF_gPanQBz431SEK6JeVLgoYtRXq_O3zDXwv7xkF6MmUbjW3Um9ZqschAhsV0PM74PhxkQ"

asins = [
    "B0C36YBG3J"
]
api = "https://advertising-api-eu.amazon.com"
country = "GB"
subject = "corralito bebe"
title = "Parque de juegos para bebés, centro de actividades para niños en interiores y exteriores con base antideslizante, patio de juegos de seguridad resistente con malla transpirable súper suave…"
description = """EL TAMAÑO MÁS ADECUADO: YOBEST ofrece una variedad de diferentes tamaños y colores de vallas para satisfacer el tamaño del espacio de diferentes familias, 150*180*69cm, 150x190x69cm, 200x200x69cm, 125*125*69cm, para proporcionar a su pequeño un espacio de juego independiente para que su pequeño gatee, camine, se ponga de pie y juegue libremente. Además, la altura científica de 69 cm no bloqueará la vista del bebé, sino que evitará que su niño gatee.
LIBERA LAS MANOS DE LA MADRE: los pequeños necesitan el cuidado de la madre todo el tiempo, sin embargo, cuando tienes varias cosas, no siempre puedes prestar atención a tu bebé. Afortunadamente, el corralito de YOBEST puede convertir cualquier lugar en un gran parque infantil seguro. Deje que sus bebés jueguen libremente, aprendan a ponerse de pie y a caminar con seguridad, ayudando a su bebé a explorar y percibir el mundo, las madres pueden soltar sus manos y hacer sus propias cosas.
SEGURIDAD Y RESISTENCIA: Los corrales de juego de YOBEST Baby están hechos de material de tela catiónica de encriptación resistente y de tubo de acero fuerte, hay 4 ventosas antideslizantes de seguridad robustas en la parte inferior, que son difíciles de mover o volcar. Al mismo tiempo, nuestra valla está completamente envuelta en tela suave, no hay peligro de pellizcos, y es más segura que el corralito de plástico para bebés.
DISEÑO DE VISIÓN 360°：Los corrales para bebés están rodeados de rejillas transparentes y transpirables. Tanto si el bebé está tumbado como sentado, puede ver a la madre fuera de la valla. La valla de juego para bebés está fuera de la cremallera para evitar que el bebé salga accidentalmente. Plus you can keep all your baby's toys in one area away from the pet hair or getting knocked over.
AFTER-SALES SERVICE: YOBEST baby fences have served more than 3.74 million families and received good market witness Easy to disassemble, assemble and storage(no tools required). If you have any questions about the product, please contact us in time, we will reply you within 8 hours.
"""
result = send_keywords_retrieval_request(api, access_token, client_id, profile_id, asins, subject, title, description,
                                         country)
print(result)
'''
ES/FR/GB/DE
'''
