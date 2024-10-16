import json
import pandas as pd

import requests


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
        # return data

        if isinstance(data, list):
            keywords = [item.get('keywordText', '') for item in data if isinstance(item, dict)]

            return keywords
        else:
            raise ValueError("Unexpected response format: Expected a list")
    else:
        response.raise_for_status()


profile_id = "2651906346803655"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIGbh3Rr1mN9BqbgAu_-gnLLTrtby0VuMkfT7O7RBfl31134bPeB0aseiWlzGMVsF_vVwsRoR9vy4fDCF9sB0QR-47H7CUXC0eiCClb341JTwK9MP6tAZPPr0--ONeE8L10mdkjgenHL8gidAL-i2lPNYpsgI8aqboMUVnhuVcC39NbAQ5i8gHhdgDzvfu44ERGPakPLsNJ6KoiFV223BGfzXHZkIVL_jT4q0OGb1O-WSau3HOM-VAbGQQTBr-sx8qU25mbIL8mGpHHGsQJm0aUR1u86fls2Ckk7WtrSQNC845nzsvTNik6A4Y_efNQ9IEKST9FtkZYV5U0OQxwZBTk2mBDGd0S2vCSAJ1wa4l21nNQGinUEYkNQ84-sBJVLEwTO585W-OP6vVLKsJjOP33oqRh93gGaxkLSgdawBQ4K-hGtyXTOfErBdx6limwRRdSv4r-ByMKLfr-lS7Rbm8K6F"
asins = ['B0D5TR7BF9']

try:
    result = get_keyword_recommendations_v2(access_token, client_id, profile_id, asins)
    print(json.dumps(result, indent=4))
except Exception as e:
    print(f'Error: {e}')
'''


'''