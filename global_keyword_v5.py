import requests


def get_global_keywords(asins, access_token, client_id, profile_id):
    request_payload = {
        "countryCodes": {
            "property1": {
                "asins": asins,
                "targets": [
                    {
                        "matchType": "BROAD",
                        "keyword": "string",
                        "bid": 0.1,
                        "userSelectedKeyword": True
                    }
                ]
            },
        },
        "biddingStrategy": "LEGACY_FOR_SALES",
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "bidsEnabled": "true",
        "maxRecommendations": "200",
        "sortDimension": "CLICKS",
        "locale": "ar_EG"
    }

    url = f"https://advertising-api-fe.amazon.com/sp/targets/keywords/recommendations"

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
