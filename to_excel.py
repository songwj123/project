import pandas as pd


def save_keywords_to_excel(result, file_name="法国-B0D6BL23MT-2.xlsx"):
    bigwords = result['data'].get('bigwords', [])
    crwords = result['data'].get('crwords', [])
    broader_words = result['data'].get('broader_words', [])
    negative_words = result['data'].get('negative_words', [])
    crwords_rank = result['data'].get('crwords_rank', {})

    # 获取大词的排名
    bigwords_data = [{'大词': word, '排名': rank} for word, rank in
                     zip(bigwords, result['data'].get('bigwords_rank', []))]

    # 获取高低转化词的排名
    crwords_data = [{'高低转化词': word, '排名': crwords_rank.get(word, None)} for word in crwords]

    data = {
        "大词": bigwords_data,
        "高低转化词": crwords_data,
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
        "bigwords": [
            "rasoir electrique femme",
            "epilateur electrique femme",
            "epilateur visage femme",
            "epilateur electrique",
            "épilateur électrique",
            "rasoir électrique femme",
            "épilateur électrique femme"
        ],
        "crwords": [
            "rasoir visage femme",
            "rasoir femme electrique",
            "epilateur electrique femme sans fil",
            "rasoir visage",
            "rasoir sourcil femme",
            "epilation visage femme",
            "rasoir femme visage",
            "rasoirs électriques femme",
            "flawless epilateur visage",
            "épilation visage femme",
            "epilateur femme",
            "epilateur moustache femme",
            "epilateur sans fil",
            "epilation visage",
            "tondeuse visage femme"
        ],
        "broader_words": [
            "rasoir electrique femme",
            "epilateur electrique femme",
            "epilateur visage femme",
            "epilateur electrique",
            "épilateur électrique",
            "rasoir électrique femme",
            "épilateur électrique femme"
        ],
        "negative_words": [
            "epilateur electrique femme maillot",
            "epilateur lumiere pulsée",
            "epilateur lumière pulsée",
            "rasoir tondeuse femme",
            "rasoir partie intime femme"
        ],
        "bigwords_rank": [
            2767,
            378,
            5282,
            8346,
            16181,
            28085,
            44248
        ],
        "crwords_rank": {
            "rasoir electrique femme": 2767,
            "epilateur visage femme": 5282,
            "epilateur electrique femme": 378,
            "epilateur electrique": 8346,
            "rasoir visage femme": 10523,
            "épilateur électrique": 16181,
            "rasoir femme electrique": 17400,
            "rasoir électrique femme": 28085,
            "epilateur electrique femme sans fil": 23536,
            "rasoir visage": 42647,
            "rasoir sourcil femme": 48952,
            "épilateur électrique femme": 44248,
            "epilation visage femme": 45334,
            "rasoir femme visage": 47668,
            "rasoirs électriques femme": 47668,
            "flawless epilateur visage": 72392,
            "épilation visage femme": 75203,
            "epilateur femme": 88391,
            "epilateur moustache femme": 101588,
            "epilateur sans fil": 106813,
            "epilation visage": 125643,
            "tondeuse visage femme": 152050
        }
    }
}

save_keywords_to_excel(result)
