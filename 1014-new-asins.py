import requests
import pandas as pd
import time
import json
from openpyxl import Workbook


# 读取Excel中的ASIN列表
def read_asins_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df['asins'].tolist()


# 请求CatalogItem接口获取排名
def get_catalog_item(asins):
    results = []
    for asin in asins:
        response = requests.get(f"http://192.168.10.160:5049/CatalogItem/{asin}")
        if response.status_code == 200:
            data = json.loads(response.json())
            if 'salesRanks' in data and data['salesRanks']:
                if 'displayGroupRanks' in data['salesRanks'][0] and data['salesRanks'][0]['displayGroupRanks']:
                    rank = data['salesRanks'][0]['displayGroupRanks'][0]['rank']
                    results.append((asin, rank))
                else:
                    print(f"ASIN {asin} 没有显示组排名。")
            else:
                print(f"ASIN {asin} 没有销售排名。")
        else:
            print(f"获取ASIN {asin} 数据时出错")
            # print(f"获取ASIN {asin} 数据时出错: {response.status_code} - {response.text}")
    return results


# 请求Amazon Advertising API获取推荐ASIN列表
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
        "locale": "zh_CN"  # 设置语言为中文
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"请求推荐ASIN时出错: {response.status_code} - {response.text}")
        return []


# 主函数
def main(excel_path, access_token, client_id, profile_id, count=47):
    asins = read_asins_from_excel(excel_path)
    highest_rank_asin = None
    highest_rank = float('inf')

    while True:
        # 获取当前ASIN列表的排名
        catalog_results = get_catalog_item(asins)
        if not catalog_results:
            break  # 如果没有获取到排名，退出循环

        catalog_results.sort(key=lambda x: x[1])  # 按排名排序
        current_best_asin, current_best_rank = catalog_results[0]

        # 检查当前排名是否更高（排名数值越小越好）
        if current_best_rank < highest_rank:
            highest_rank_asin = current_best_asin
            highest_rank = current_best_rank

        # 获取推荐的ASIN列表
        recommended_asins = get_asins(access_token, client_id, profile_id, [highest_rank_asin], count)

        if recommended_asins:
            asins = recommended_asins  # 更新ASIN列表
        else:
            break  # 如果没有推荐的ASIN，退出循环

        time.sleep(1)  # 防止请求过于频繁

    # 保存最高排名ASIN及其推荐ASIN到Excel
    output_data = {
        '最高排名ASIN': [highest_rank_asin],
        '推荐ASIN': [recommended_asins]  # 将推荐ASIN作为列表存储
    }
    output_df = pd.DataFrame(output_data)
    output_df.to_excel('highest_rank_asin_and_recommendations.xlsx', index=False)
    print(f"最高排名的ASIN: {highest_rank_asin}, 推荐ASIN数量: {len(recommended_asins)}")


if __name__ == "__main__":
    # 需要传入的参数
    excel_path = '1014B0D8Q15LPC.xlsx'
    access_token = "Atza|IwEBIB1c7s4PT4E0naal4dF95g2cnVF2l2Ydkt8vcsRBAkx3B5FRgZ1oMjAoTxZOZTh7ru5wZBxSWGPDSePUbMVSzQCIh4ftimapOYC9DNgEQDTrOtDszGL7dYsulzG1N_9za2ERKDBKr3RO4JkNrRxzvUj4s8G79DAgV2jnJTPRp2hbU9QdSi9uBrTTNhzJYfZz99assvya4sH2Z1nEWMoepa5AuZuRNVoFNgFNAvscKloi6xTlbUtc5UjF8t51fAg4URWfrPXi7qnOqXKI5V7PidEKVsVEi9SrNk-YcwPhOivs_gxPLuesbNzSQ1Q-S6nDYR4Bx3GcF6D90sSHSZZTrmAX_7raR2h1whr1rUefx-KO1sCe8-2MyEvCxnIeSsRuILFEqKUgaP_pFGrHzYt0D3vp1VB-DYcUnyGMbAI009UqmuJTiYK1JZ0oQ33C0QjNnBci3Z7U_XVRl3YWN_uRL0sZ"
    client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
    profile_id = "2651906346803655"

    main(excel_path, access_token, client_id, profile_id)
