import requests
import json
import pandas as pd


def get_keyword_recommendations(asins, access_token, client_id, profile_id, host):
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,  # 最大推荐数量
        "sortDimension": "CLICKS",  # 排序维度，使用 {“CONVERSIONS", "CLICKS"} 进行排序
        "locale": "it_IT",  # 语言设置
        "biddingStrategy": "AUTO_FOR_SALES",  # 出价策略
        "bidsEnabled": True,  # 是否启用出价建议
    }

    url = f"{host}/sp/targets/keywords/recommendations"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v5+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v5+json'
    }

    try:
        response = requests.post(url=url, headers=headers, json=request_payload)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}


# def save_to_excel(data, filename):
#     # 展开数据
#     expanded_data = []
#     for item in data:
#         expanded_item = item.copy()
#         # 展开 suggestedBid 字段
#         suggested_bid = expanded_item.pop('suggestedBid', {})
#         expanded_item.update({
#             'suggestedBid_rangeStart': suggested_bid.get('rangeStart'),
#             'suggestedBid_rangeMedian': suggested_bid.get('rangeMedian'),
#             'suggestedBid_rangeEnd': suggested_bid.get('rangeEnd'),
#             'suggestedBid_bidRecId': suggested_bid.get('bidRecId')
#         })
#         # 添加到列表中
#         expanded_data.append(expanded_item)
#
#     # 创建 DataFrame
#     df = pd.DataFrame(expanded_data)
#
#     # 保存到 Excel 文件
#     df.to_excel(filename, index=False)
#     print(f"数据已保存到 {filename}")


asins = [
    'B0D2NGK7SB'
]
profile_id = "3218265756783695"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIPAf5EJ9Zg9lET5Osb51Yp_EjPmScoom2n9AfX597atVs5cDCOBDBjRLV_tVcGh4rUZCOxhDnb-SrTjMsQfHLM6csm2p2UpxryQ1BObrHudanCJGX_Jmprg9GaHGia-dTT2Yq-E1cO8I6KGyOe_H2ifkD2RWGdIitmLLpdmqth40Plx2bKt34u3ru4mGRprJzGD9t1rKd4LUQXhGaPXS-IonyQd_mex7dfCPrYDxh9qMc4ZaBxv1mjG1396D-ufy78fPflTbwRExKVMKG8TW1ny8OFnGyymwitg3hGNOtKq9o2RkJluHM2X_7hmKVuCchr6yEA2jb8OdCeD6JA6rhUSkxnKFJ6tdLikc7Ntq3zpMYbMxRpqk5x9gaoSnd_FNit0ByRBqKi60cGK-N4ZEnYnkdGfhBmgyswv8LmGPgjL62C9og_fK1l90LCKH9IF_4hvHVgPHrDNG-2xPN6GAxhUcuyQdRafH0Pw_dHQ7Afsa_UBD1rL_SFxI0F1UZvjOUwGBOVzJfMCthOWjLpUGzZaheY00pCdYdD7TUPdOTAuBcQ"
host = "https://advertising-api.amazon.com"
result = get_keyword_recommendations(asins, access_token, client_id, profile_id, host)
print(json.dumps(result, indent=2))

# if 'error' in result:
#     print(result['error'])
# else:
#     # 保存结果到 Excel 文件
#     save_to_excel(result, 'CA_B0D9B7VV9B-v5.xlsx')

