import json
import pandas as pd

import requests


def get_suggested_keywords(asins, max_suggestions, access_token, client_id, profile_id, api_endpoint):
    # 构建API请求头
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/json'
    }

    # 构建请求参数
    params = {
        'maxNumSuggestions': max_suggestions
    }

    # 发送API请求
    response = requests.get(f'{api_endpoint}/sp/asins/{asins}/suggested/keywords', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if isinstance(data, list):
            # return data
            keywords = [item.get('keywordText', '') for item in data if isinstance(item, dict)]

            return {
                'keywordTexts': keywords,

                # 'count': len(keywords)
            }
        else:
            raise ValueError("Unexpected response format: Expected a list")
    else:
        response.raise_for_status()  # 抛出异常


def save_keywords_to_excel(keywords, file_name):
    # 数据转换
    df = pd.DataFrame({'Keyword': keywords})

    # 保存Excel文件
    df.to_excel(file_name, index=False)


profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIEizbVmJq1VCLs9ucpNBSFDhRD8PvMn2fMKUSNmRw6C4S4WioCQuOV5M7eXJ0WJWUuE-cN3_ttdRVrGQcHVsRrNVCDr0R8NufbyIVVGT2Xz8ye05idVUd74ey3qFdCd7gQh7PIiKrvihOPhiyJG8YpoTWKFd8wpGdjPB43-1ZicW3OXCSZqp7SE_W-xecXZzm6plnronnNrL25eNOQufUAomOjf5JM-IfSoU6P9g3gBfIHTEbTwhCtG0BhsdiBEK9FKhec_FxhN2iK-l-t454CXCgW-kNvLE2qVZOMB-XmH1hV16Jq8vZ7fhJAlr64BKghQ1sNOn59dVzRHalEvehBZMtSj4g0jqqRH4InHJiGpVhBUbusuCkh8aOdXAsP84tTvBP-oanO-4ygfL2sh0LrPzo9JuHVdjubNLbUDi5WSRUBTuXZ3toWDh6p2eG_vCdwF24Xs41gyCTRir4M7DWy_b"
api_endpoint = 'https://advertising-api.amazon.com/v2'
asins = 'B0CW3FSBVT'
max_suggestions = 1000
excel_file = 'cs-v2.xlsx'

try:
    result = get_suggested_keywords(asins, max_suggestions, access_token, client_id, profile_id, api_endpoint)
    keywords = result['keywordTexts']
    save_keywords_to_excel(keywords, excel_file)
    # print(json.dumps(result, indent=4))
    print(f'Successfully saved {len(keywords)} keywords to {excel_file}.')
except Exception as e:
    print(f'Error: {e}')


'''


'''