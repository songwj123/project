import requests


def get_suggested_keywords(api_host, access_token, client_id, profile_id, asins, max_num_suggestions=1000):
    url = f"{api_host}/v2/sp/asins/suggested/keywords"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Amazon-Advertising-API-ClientId": client_id,
        "Amazon-Advertising-API-Scope": profile_id,
        "Content-Type": "application/json"
    }

    payload = {
        "asins": asins,
        "maxNumSuggestions": max_num_suggestions
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "code": response.status_code,
            "details": response.text
        }


# 示例调用
asins = [
    'B0BHRZBHNX'
]
profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBICJ8yH6btSS7DTmdqS9RKylKMY9fbouT_gtcp7Q7PTSvU-a81Mn1zw52XuYE40OZpj4SfJnxSEuBrSVaeYzITpBpVwvpCa1-bMm9hYtbXdQNTeRhV3dmqe3hdO_Sduo2iMTX7HjkK5VgMJfaU3YvRTqdyO6q8RKigtEZTfWV13mHGe2wau6GnPgfcVW5vWqgDQ2Co74KOljVd4egKAFcFaC2BhQA-ZCBhQ1-A251CXN7BzpcXVnNc8RqWPdkGvFKwU6ONfQ3TuWUbC3Xio5Q_71WXOiTTm7a5wbpK1UUczh3I4Rmqw_lUI7Z9GuP86G8Ky-xjYD1cj875-PzVV9eywEgLxRmvyr98Z5GYpiCraM3Q49xbTHX1lK5M4P_6z1tcYKEgCdZipmeBIVtddzPove-zXslMnZOuk772KOhocDZV7lcmBSXBmke_y_1RbWSCygnxxM7rpJj6ZDIvl9w1ONQ6iXDProyw-_OtUNmc60vOw"
host = "https://advertising-api.amazon.com"

keywords = get_suggested_keywords(host, access_token, client_id, profile_id, asins)
print(keywords)
