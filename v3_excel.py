import pandas as pd

# 数据
data = {'code': 0, 'msg': 'success', 'data': {'bigwords': [],
                                              'crwords': ['best bald head shaver', 'razor men electric shaver',
                                                          'pitbull skull shaver', 'skull shaver',
                                                          'shavers for men razor', 'remington head shaver',
                                                          'best shaver for bald head'], 'broader_words': [],
                                              'negative_words': ['bulldog shaver', 'grooming kit', 'bulldog razor',
                                                                 'tondeuse pour chauve', 'rasoir électrique homme',
                                                                 'rasoir tete chauve homme', 'rasoir tete homme',
                                                                 'rasoir crane homme', 'rasoir chauve',
                                                                 'rasoir tete chauve', 'electric shaver men',
                                                                 'rasoir tete', 'rasoir electrique homme', 'manscaped',
                                                                 'hatteker', 'tondeuse homme', 'menscape', 'olov',
                                                                 'hair buzzer for men', 'ball shaver men',
                                                                 'trimmer wahl', 'philips body groomer', 'mangroomer',
                                                                 'manscaped 4.0', 'silky glide shaver',
                                                                 'shavers for men balls', 'brio beardscape v2',
                                                                 'ball shaver', 'mens body trimmer', 'manscaped 3.0',
                                                                 'remington shaver', 'best nose hair trimmer',
                                                                 'weed eater head', 'razoire barbe homme',
                                                                 'rasoir electrique homme barbe',
                                                                 'ladies electric shaver', 'brightup beard trimmer',
                                                                 'elorixa shaver'], 'bigwords_source_rank': {},
                                              'crwords_source_rank': {
                                                  'best bald head shaver': {'rank': 169615, 'src': ['vec', 'v2v3']},
                                                  'razor men electric shaver': {'rank': 39291, 'src': ['v2v3']},
                                                  'pitbull skull shaver': {'rank': 29387, 'src': ['v2v3']},
                                                  'skull shaver': {'rank': 199007, 'src': ['vec']},
                                                  'shavers for men razor': {'rank': 188284, 'src': ['vec']},
                                                  'remington head shaver': {'rank': 181668, 'src': ['vec']},
                                                  'best shaver for bald head': {'rank': 164209, 'src': ['vec']}},
                                              'cost': 96.45281600789167}}

data = data
# 提取bigwords_rank数据
bigwords = []
big_srcs = []
big_ranks = []

for word, details in data['data']['bigwords_source_rank'].items():
    bigwords.append(word)
    big_srcs.append(", ".join(details["src"]) if details["src"] else "None")
    big_ranks.append(details["rank"])

# 提取crwords_rank数据
crwords = []
cr_srcs = []
cr_ranks = []

for word, details in data['data']['crwords_source_rank'].items():
    crwords.append(word)
    cr_srcs.append(", ".join(details["src"]) if details["src"] else "None")
    cr_ranks.append(details["rank"])

# 创建DataFrame
bigwords_df = pd.DataFrame({
    "bigwords": bigwords,
    "Source": big_srcs,
    "Rank": big_ranks
})

crwords_df = pd.DataFrame({
    "crwords": crwords,
    "Source": cr_srcs,
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
output_file = "DE-1107-B0B7X8H1B5.xlsx"
# df.to_excel(output_file, index=False)

# print(f"Data saved to {output_file}")

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, keywords in data.items():
        df = pd.DataFrame(keywords)
        df.to_excel(writer, sheet_name=sheet_name, index=True)
