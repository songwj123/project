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

    # 构建请求参数
    data = {
        'asins': asins,
        'matchType': 'broad',
        'maxNumSuggestions': max_suggestions
    }

    url = f'https://advertising-api.amazon.com/v2/sp/asins/suggested/keywords'

    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}


profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIBXdxMCasKsyNxuJEMXE-yFAiXufXHm8ut75rmrYx3Eui6hKc-spNADd67gxYSlOF87b43cmc54EoEZpXk_wqlgf5_GMX_4X2fCyyVdXvhZR_4P7Yy_N_s_K2zfOnaC1ooQO9Olsd-AT4l4TJ26ZPR4hE1j3Ym3XkgtfROCSbAk2QSu1JAOyjlU2qwog_H1J3UhTlcHnvEMkPyN8S0k2FjbtWur2PyfpuPsTOLAQaE_7kcyKIkKoNti2iCwpV_bhJBYqUMLfFhtvUwPlgJvRylZ764rGRcumVKCwLyRN-1dul5UFvBe-4ksWZikfgY2eDdFhfrzLai5CcCH5R91uRF6owN-AmLJrZhNX5YzXnrYUUSBs_KCaZzWjYcRdvu3NTWolC8CQUMijtulptfTJBlCAJ8U6k0LRBH1-kbB4UwJ_zTGTTqcBwoYauGFD2TzC0m7YUiDGcoZJpacwMNymIpInjig_isbJf-1E_ZdZ3O4mKw"
asins = ['B0CJM9FD8P']  # ASIN
max_suggestions = 1000  # 最大建议数量
result = get_suggested_keywords(asins, max_suggestions, access_token, client_id, profile_id)
print(json.dumps(result, indent=4))
