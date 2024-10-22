import pandas as pd

# 数据
data = {'data': {'bigwords': ['flawless facial hair remover'],
                                                      'crwords': ['hair removal device', 'hair removal',
                                                                  'finishing touch flawless', 'face shaver',
                                                                  'facial hair remover', 'hair remover',
                                                                  'upper lip hair removal', 'flawless hair remover',
                                                                  'women facial hair remover', 'facial hair removal',
                                                                  'women face shaver', 'face hair remover',
                                                                  'face hair removal', 'mustache trimmer women',
                                                                  'women face shaver peach fuzz', 'peach fuzz remover',
                                                                  'flawless hair removal', 'female facial hair remover',
                                                                  'women hair removal', 'face hair trimmer',
                                                                  'womens mustache hair remover',
                                                                  'women facial hair trimmer',
                                                                  'face hair removal device',
                                                                  'womens facial hair remover device',
                                                                  'female face shaver peach fuzz',
                                                                  'women facial hair removal device',
                                                                  'flawless rechargeable facial hair remover',
                                                                  'women mustache shaver', 'chin hair remover',
                                                                  'womens facial hair razor',
                                                                  'depiladora facial para mujer',
                                                                  'womens face shaver peach fuzz',
                                                                  'painless hair removal for women',
                                                                  'flawless hair remover for face',
                                                                  'flawless finishing touch',
                                                                  'womens face hair remover',
                                                                  'electric face razors for women',
                                                                  'mustache shavers for women',
                                                                  'electric shaver for women face',
                                                                  'womens facial shaver', 'womens facial hair removal',
                                                                  'depiladora de bigote para mujer'],
                                                      'broader_words': ['flawless facial hair remover'],
                                                      'negative_words': ['plucy facial hair remover',
                                                                         'hero epilator facial hair removal',
                                                                         'conture hair removal tool',
                                                                         'gurelax facial hair removal for women'],
                                                      'bigwords_rank': {'flawless facial hair remover': 4517},
                                                      'crwords_rank': {
                                                          'hair removal device': {'src': ['v2', 'v3'], 'rank': 12984},
                                                          'flawless facial hair remover': {'src': ['v3'], 'rank': 4517},
                                                          'hair removal': {'src': ['v3'], 'rank': 21831},
                                                          'finishing touch flawless': {'src': ['v3'], 'rank': 35304},
                                                          'face shaver': {'src': ['v2', 'v3'], 'rank': 37663},
                                                          'facial hair remover': {'src': ['v2', 'v3'], 'rank': 66713},
                                                          'hair remover': {'src': ['v2', 'v3'], 'rank': 58696},
                                                          'upper lip hair removal': {'src': ['v3'], 'rank': 128014},
                                                          'flawless hair remover': {'src': ['v3'], 'rank': 138347},
                                                          'women facial hair remover': {'src': ['v2', 'v3'],
                                                                                        'rank': 202277},
                                                          'facial hair removal': {'src': ['v2', 'v3'], 'rank': 205014},
                                                          'women face shaver': {'src': ['v2', 'v3'], 'rank': 264788},
                                                          'face hair remover': {'src': ['v2', 'v3'], 'rank': 280413},
                                                          'plucy facial hair remover': {'src': ['v2'], 'rank': 364961},
                                                          'face hair removal': {'src': ['v2', 'v3'], 'rank': 399632},
                                                          'hero epilator facial hair removal': {'src': None,
                                                                                                'rank': 426313},
                                                          'mustache trimmer women': {'src': None, 'rank': 417993},
                                                          'women face shaver peach fuzz': {'src': ['v3'],
                                                                                           'rank': 459849},
                                                          'peach fuzz remover': {'src': ['v3'], 'rank': 535925},
                                                          'flawless hair removal': {'src': None, 'rank': 623612},
                                                          'female facial hair remover': {'src': ['v2', 'v3'],
                                                                                         'rank': 864211},
                                                          'women hair removal': {'src': ['v3'], 'rank': 864211},
                                                          'face hair trimmer': {'src': ['v2'], 'rank': 887533},
                                                          'womens mustache hair remover': {'src': ['v2'],
                                                                                           'rank': 1042132},
                                                          'women facial hair trimmer': {'src': ['v2'], 'rank': 1112736},
                                                          'face hair removal device': {'src': ['v2', 'v3'],
                                                                                       'rank': 1311011},
                                                          'womens facial hair remover device': {'src': ['v2'],
                                                                                                'rank': 1285581},
                                                          'female face shaver peach fuzz': {'src': ['v3'],
                                                                                            'rank': 1632429},
                                                          'women facial hair removal device': {'src': ['v2', 'v3'],
                                                                                               'rank': 1632429},
                                                          'flawless rechargeable facial hair remover': {
                                                              'src': ['v2', 'v3'], 'rank': 1715421},
                                                          'women mustache shaver': {'src': ['v3'], 'rank': 1857948},
                                                          'chin hair remover': {'src': ['v2'], 'rank': 2152601},
                                                          'womens facial hair razor': {'src': ['v2'], 'rank': 2221966},
                                                          'depiladora facial para mujer': {'src': ['145w'],
                                                                                           'rank': 171877},
                                                          'womens face shaver peach fuzz': {'src': ['145w'],
                                                                                            'rank': 611855},
                                                          'painless hair removal for women': {'src': ['145w'],
                                                                                              'rank': 636131},
                                                          'flawless hair remover for face': {'src': ['145w'],
                                                                                             'rank': 821149},
                                                          'flawless finishing touch': {'src': ['145w'], 'rank': 864211},
                                                          'womens face hair remover': {'src': ['145w'], 'rank': 925162},
                                                          'electric face razors for women': {'src': ['145w'],
                                                                                             'rank': 965759},
                                                          'mustache shavers for women': {'src': ['145w'],
                                                                                         'rank': 980129},
                                                          'electric shaver for women face': {'src': ['145w'],
                                                                                             'rank': 1059020},
                                                          'conture hair removal tool': {'src': ['145w'],
                                                                                        'rank': 1364851},
                                                          'womens facial shaver': {'src': ['145w'], 'rank': 1364851},
                                                          'gurelax facial hair removal for women': {'src': ['145w'],
                                                                                                    'rank': 1364851},
                                                          'womens facial hair removal': {'src': ['145w'],
                                                                                         'rank': 1423306},
                                                          'depiladora de bigote para mujer': {'src': ['145w'],
                                                                                              'rank': 1486915}}},
        'big-keyword-targeting': 0.07, 'cr-keyword-targeting': 1.81, 'broader-keyword-targeting': 0.12,
        'negative-broader-targeting': None, 'negative-auto-a-targeting': None, 'product-create': 185, 'ads-conf': None}
data = data
# 提取bigwords_rank数据
bigwords = []
big_ranks = []

for word, rank in data['data']['bigwords_rank'].items():
    bigwords.append(word)
    big_ranks.append(rank)

# 提取crwords_rank数据
crwords = []
srcs = []
cr_ranks = []

for word, details in data['data']['crwords_rank'].items():
    crwords.append(word)
    srcs.append(", ".join(details["src"]) if details["src"] else "None")
    cr_ranks.append(details["rank"])

# 创建DataFrame
bigwords_df = pd.DataFrame({
    "Word": bigwords,
    "Source": "145w",
    "Rank": big_ranks
})

crwords_df = pd.DataFrame({
    "Word": crwords,
    "Source": srcs,
    "Rank": cr_ranks
})

# 排序 由小到大
bigwords_df = bigwords_df.sort_values(by="Rank", ascending=True).reset_index(drop=True)
crwords_df = crwords_df.sort_values(by="Rank", ascending=True).reset_index(drop=True)

data = {
    "大词排名": bigwords_df,
    "高低转化词排名": crwords_df
}

# 合并两个DataFrame
# df = pd.concat([bigwords_df, crwords_df], ignore_index=True)
#
# # 保存到Excel
output_file = "1021-B0D22PK14W.xlsx"
# df.to_excel(output_file, index=False)

# print(f"Data saved to {output_file}")

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, keywords in data.items():
        df = pd.DataFrame(keywords)
        df.to_excel(writer, sheet_name=sheet_name, index=True)
