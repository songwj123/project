import json
import pandas as pd

import requests


def get_suggested_keywords(asins, max_suggestions, access_token, client_id, profile_id):
    # 构建API请求头
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/json'
    }

    params = {
        'maxNumSuggestions': max_suggestions
    }

    response = requests.get(f'https://advertising-api.amazon.com/v2/sp/asins/{asins}/suggested/keywords', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            keywords = [item.get('keywordText', '') for item in data if isinstance(item, dict)]

            return {
                'keywordTexts': keywords
            }
        else:
            raise ValueError("Unexpected response format: Expected a list")
    else:
        response.raise_for_status()  # 抛出异常


profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIG3mYM3zcBrnWRSeSmPp2KthBcHRuQ5-SG9QwfXVzo6x2sNR1BG054yG_ZyBXwLVitqYMf5SKhteQ-nqZ8TE7ulyCL-P-LlC_hCk8me7tROMHiawMJfgIvk8snaSy8r9O52eQMeXE7eMAt1xW5DomrqQcSWAWxULMZlbOy1eUG4VyrscYWyWOV9f32K76BX_epqaD4aBS80gbqyYnwnY7iQmVyhGKl2kDsGalpQEnp3ejxVUotC_VXAa78qu8xjEHTLxdZI2NECdHbB4FwpUkA4JbJN59Hq8KJBtfdf73wU3iPnRjSuTsNBwaqdBS6qsIiC0R6g-0VXZ06F03mk80rA0wN9XXZt3XSeOwI-MM4WnajouWjrhM4irmKxfOQgNvU6fbYPZ_XSmxb2X1fafwCcThLdTbEYY4YLKwvoKY1wkU8q5Km4NpT4mq8nSsNjCkXopMX-w9xsX1UlEfe9Eaj7l2LCynQrcNyD_VDcpUThQvg"
api_endpoint = 'https://advertising-api.amazon.com/v2'
asins = 'B0BXPFSMPL'
max_suggestions = 1000

try:
    result = get_suggested_keywords(asins, max_suggestions, access_token, client_id, profile_id)
    print(json.dumps(result, indent=4))
except Exception as e:
    print(f'Error: {e}')
