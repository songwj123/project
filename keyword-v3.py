import requests
import json
import pandas as pd


def get_keyword_recommendations(asins, access_token, client_id, profile_id, host):
    request_payload = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,  # 最大推荐数量
        "sortDimension": "CLICKS",  # 排序维度，使用 {“CONVERSIONS", "CLICKS"} 进行排序
        "locale": "en_US",  # 语言设置
        "biddingStrategy": "AUTO_FOR_SALES",  # 出价策略
        "bidsEnabled": True,  # 是否启用出价建议
    }

    url = f"{host}/sp/targets/keywords/recommendations"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Amazon-Advertising-API-ClientId': client_id,
        'Amazon-Advertising-API-Scope': profile_id,
        'Content-Type': 'application/vnd.spkeywordsrecommendation.v3+json',
        'Accept': 'application/vnd.spkeywordsrecommendation.v3+json'
    }

    try:
        response = requests.post(url=url, headers=headers, json=request_payload)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"Other error occurred: {err}"}


def save_to_excel(data, filename):
    # 展开数据
    expanded_data = []
    for item in data:
        expanded_item = item.copy()
        # 展开 suggestedBid 字段
        suggested_bid = expanded_item.pop('suggestedBid', {})
        expanded_item.update({
            'suggestedBid_rangeStart': suggested_bid.get('rangeStart'),
            'suggestedBid_rangeMedian': suggested_bid.get('rangeMedian'),
            'suggestedBid_rangeEnd': suggested_bid.get('rangeEnd'),
            'suggestedBid_bidRecId': suggested_bid.get('bidRecId')
        })
        # 添加到列表中
        expanded_data.append(expanded_item)

    # 创建 DataFrame
    df = pd.DataFrame(expanded_data)

    # 保存到 Excel 文件
    df.to_excel(filename, index=False)
    print(f"数据已保存到 {filename}")


asins = [
    'B0BXPFSMPL'
]
profile_id = "3854189483301387"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIG3mYM3zcBrnWRSeSmPp2KthBcHRuQ5-SG9QwfXVzo6x2sNR1BG054yG_ZyBXwLVitqYMf5SKhteQ-nqZ8TE7ulyCL-P-LlC_hCk8me7tROMHiawMJfgIvk8snaSy8r9O52eQMeXE7eMAt1xW5DomrqQcSWAWxULMZlbOy1eUG4VyrscYWyWOV9f32K76BX_epqaD4aBS80gbqyYnwnY7iQmVyhGKl2kDsGalpQEnp3ejxVUotC_VXAa78qu8xjEHTLxdZI2NECdHbB4FwpUkA4JbJN59Hq8KJBtfdf73wU3iPnRjSuTsNBwaqdBS6qsIiC0R6g-0VXZ06F03mk80rA0wN9XXZt3XSeOwI-MM4WnajouWjrhM4irmKxfOQgNvU6fbYPZ_XSmxb2X1fafwCcThLdTbEYY4YLKwvoKY1wkU8q5Km4NpT4mq8nSsNjCkXopMX-w9xsX1UlEfe9Eaj7l2LCynQrcNyD_VDcpUThQvg"
host = "https://advertising-api.amazon.com"
result = get_keyword_recommendations(asins, access_token, client_id, profile_id, host)
# print(json.dumps(result, indent=2))

if 'error' in result:
    print(result['error'])
else:
    # 保存结果到 Excel 文件
    save_to_excel(result, 'B0BXPFSMPL-v3.xlsx')

