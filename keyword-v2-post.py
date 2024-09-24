import json
import pandas as pd

import requests


def get_keyword_recommendations_v2(access_token, client_id, profile_id, asins):
    url = "https://advertising-api-eu.amazon.com/v2/sp/asins/suggested/keywords"
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


profile_id = "4377063015685477"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIMBk4SYkmoSWTe4_r4enjAXiWWkdDkkI6TLLnffOi0qTfgbu-oDv5DW3GNHNDl0hysIIvz7JCZR6lXyIRAyyJG4VW1BToiymSZiZj4InGSYG4mXwcgkPmBv3pPcrf46Je5tc0yzTt0d3OwJuvpVxn15qT_Li48fFqO9t9kccdwwYewE2ECF3h3LPgHr9q9lBjevtYJzRVnQ3k2zNtaMIV2lUOLVm-YnljP0AuZgnnCSblWP-asUuWb2GYHGnuoIjCl_kE4_ZfXHbqLw62cO1Ctkdgjm7x6pHDHpcM9HLKFdJH3aIodpwGkd4QnWpwokFTURDEfr5-2ioRYu-KHqPJznwrRUIw50Yx7OcGOcoQ1rRn5h-IsfmEHEFjG5osC2qpixtLRREo2bn7ujDGLpyX_zV5DaIGtvzYQcSUY-P_oQ_3KjKXsg6dO4YAfXPKitdUZmb5joUMICxOGJWv7qsuXBK"

asins = [
    "B0D6VT58SM"
]

try:
    result = get_keyword_recommendations_v2(access_token, client_id, profile_id, asins)
    print(json.dumps(result, indent=4))
except Exception as e:
    print(f'Error: {e}')
