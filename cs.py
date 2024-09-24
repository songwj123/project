import pandas as pd


def save_keywords_to_excel(result, file_name="德国-B0D6VT58SM.xlsx"):
    bigwords = result['data'].get('bigwords', [])
    crwords = result['data'].get('crwords', [])
    broader_words = result['data'].get('broader_words', [])
    negative_words = result['data'].get('negative_words', [])
    crwords_rank = result['data'].get('crwords_rank', {})

    def get_rank_data(words, rank_data):
        data = []
        for word in words:
            rank = rank_data.get(word, None)
            data.append({'高转化词': word, '排名': rank})
        return data

    # 处理大词，如果 bigwords 和 bigwords_rank 都为空则不需要生成数据
    bigwords_data = [{'大词': word, '排名': None} for word in bigwords]

    # 处理高转化词
    crwords_data = get_rank_data(crwords, crwords_rank)

    data = {
        "大词": bigwords_data,
        "高转化词": crwords_data,
        "广泛词": [{'广泛词': word} for word in broader_words],
        "否定词": [{'否定词': word} for word in negative_words]
    }

    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        for sheet_name, keywords in data.items():
            df = pd.DataFrame(keywords)

            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"数据已成功保存到 {file_name}")


result = {
    "code": 0,
    "msg": "success",
    "data": {
        "bigwords": [],
        "crwords": [
            "head shaver",
            "hair shaver",
            "kopfrasierer glatze",
            "glatzen rasierer",
            "konturen rasierer herren",
            "kopf rasierer herren",
            "rotationsrasierer für herren",
            "rasierer elektrisch herren",
            "rasierer glatze",
            "rasierer kopf glatze",
            "glatzen rasierer herren 0 mm",
            "rasierer herren elektrisch kopf",
            "nassrasierer herren elektrisch",
            "kopf rasierer",
            "rasierer glatze herren",
            "head shaver men",
            "kopfrasierer glatze 0 mm",
            "rasierer für glatze",
            "kopfrasierer 1mm"
        ],
        "broader_words": [],
        "negative_words": [
            "haarschneidemaschine für glatze"
        ],
        "bigwords_rank": [],
        "crwords_rank": {
            "head shaver": 157558,
            "hair shaver": 445121,
            "kopfrasierer glatze": 32793,
            "glatzen rasierer": 40040,
            "konturen rasierer herren": 72239,
            "kopf rasierer herren": 109187,
            "rotationsrasierer für herren": 110376,
            "rasierer elektrisch herren": 149003,
            "rasierer glatze": 159790,
            "rasierer kopf glatze": 196738,
            "glatzen rasierer herren 0 mm": 211610,
            "rasierer herren elektrisch kopf": 219912,
            "nassrasierer herren elektrisch": 228852,
            "kopf rasierer": 238570,
            "rasierer glatze herren": 279668,
            "head shaver men": 325986,
            "kopfrasierer glatze 0 mm": 365524,
            "rasierer für glatze": 388888,
            "haarschneidemaschine für glatze": 429463,
            "kopfrasierer 1mm": 445121
        }
    }
}

save_keywords_to_excel(result)
