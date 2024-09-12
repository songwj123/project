import requests
import json
import pandas as pd
from openpyxl import Workbook


def get_asins(access_token, client_id, profile_id, asins, count):
    url = "https://advertising-api.amazon.com/sp/targets/products/recommendations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spproductrecommendation.v3+json',
        'Accept': 'application/vnd.spproductrecommendation.v3+json'
    }
    data = {
        "adAsins": asins,
        "count": count,
        "locale": "en_US"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIJYKumJHczTPWTj8-rD0-b0u5mFcWvNqSrvPBxqeeB5q4_U4jBNTHAzAtL2sULxOuQxsaE3haU85NcomYXRI5vZ7yO419u1EkvZp1X1ZFbKf24l1so1uHjBGmt_N0NHvQgJuUE1d_X-9kbpzOiigdK9BvKkX77MV9e6DYvnoK1_wPF-htWaxns7fk612zRco_gHn-SaAYsySwMrbuv1aMpN8-629p-PaOpN_twD0WfHjeAeyF20k-ugO0M5PHA_xXbymjwy7ZznHlVJ_aeiF0b8Hw4X_MOlVxYkCbsA0xFiXE6G0N4jv76eg9NLR-LdY-DjT9FpQacz6ogq53ZTpCsaYmR0WOJ8rZLnjPV6SeokY_TIWzNY5mcV0J_hWM7NXq1SQHuo7_FUWGOnDAF8pCxgFPsXmrcS281q1VMPmExt-yQnQbjiISUGxS-7U4QDmMhmKzqX1sdWCwSs6yfGYX4JjbhLUv9XWuWqBDiilE85Wkw"
asins = ['B0CZP2ZJV2']
count = 47
result = get_asins(access_token, client_id, profile_id, asins, count)
print(result)

data = {"company_id": "3854189483301387", "user_info": f"'NA:advertising:901723440409076962'", "marketplace": "US",
        "profile_id": "3854189483301387"}

'''
https://affiliate-us.tiktok.com/api/v1/insights/affiliate/creator/search/suggestions?user_language=en&aid=4331&app_name=i18n_ecom_alliance&device_id=0&fp=verify_lzt7u0mm_ey148nR0_8yLR_4RqY_8tWx_isv7TuUKvvuF&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F128.0.0.0+Safari%2F537.36&browser_online=true&timezone_name=Asia%2FShanghai&oec_seller_id=7495198257562749707&shop_region=US


'''
