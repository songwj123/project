import openpyxl
import requests
import json
import pandas as pd
from openpyxl import Workbook


def get_asins(access_token, client_id, profile_id, asins, count):
    url = "https://advertising-api-eu.amazon.com/sp/targets/products/recommendations"
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
        "locale": "es_ES"
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_json = response.json()
        # return response_json
        recommended_asins = [item['recommendedAsin'] for item in response_json.get('recommendations', [])]
        return recommended_asins
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []


# 将推荐的 ASIN 列表保存到 Excel 文件
# def save_asins_to_excel(asins, file_name):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.title = "ASINs"
#
#     # 在第一行添加标题
#     sheet.cell(row=1, column=1, value="推荐的ASIN")
#
#     # 从第二行开始写入ASIN
#     for idx, asin in enumerate(asins, start=2):
#         sheet.cell(row=idx, column=1, value=asin)
#
#     workbook.save(file_name)
#     print(f"已保存{file_name}")


# 整合两个功能
# def fetch_and_save_asins(access_token, client_id, profile_id, asins, count, file_name):
#     recommended_asins = get_asins(access_token, client_id, profile_id, asins, count)
#     if recommended_asins:
#         save_asins_to_excel(recommended_asins, file_name)


profile_id = "1724874051069213"
client_id = "amzn1.application-oa2-client.8c1b204420b3431382419c27cb5e1243"
access_token = "Atza|IwEBIKfDJV6YtbeXd90pEIhjZOsOdMRz_Ga0YJUNlEcwVm3Newk0jK9MkM7Oo2grrtRCgbKlBZsICKMNwaPGkXWjamdhAOE-8AY-I8X2u352DJV2nSp7SuwetzvEQQZMkLyWPkiVh4JEViH1dnxEwtcBN8d9TYMuJTAW324fgnLEpgl_AiIo698npvmJDW7UFymnlGZiyo8hOPaTV4udW3VvlH73bnp29L5r81wmSrktjlFaQOaHN5tpOi8_88mvOSnWjcBKHiNJQ3FVc1q6HwOJNOIuBKi0yEIRnGady9cF1vmfvSdPWN3NMSuoUy5gpfZD-YcveyLBNIl0EEPC8KA6lKHpZ6AIl4C9oW-IkwlXsnQAvaeJwu_U0v-eCicqD8-URRg6P3_cA___6vwisNNDLA34oHMgsvgb1VZnEcM4kLiEo9ZxhjtJtxZplsggwF1dl1-7b4Qvozs7HTuNeyUrqlLX5LmF8rbgN0_FWkJRGVWQZQ"
asins = ['B08LSW56MZ']
count = 47
file_name = f"法国-{asins[0]}.xlsx"
result = get_asins(access_token, client_id, profile_id, asins, count)
print(json.dumps(result, indent=4, ensure_ascii=False))
# fetch_and_save_asins(access_token, client_id, profile_id, asins, count, file_name)
# print(result)
#
# data = {"company_id": "3854189483301387", "user_info": f"'NA:advertising:901723440409076962'", "marketplace": "US",
#         "profile_id": "3854189483301387"}

