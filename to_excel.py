import pandas as pd


def save_keywords_to_excel(result, file_name="法国-B0D5Y7FBF4.xlsx"):
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
        "bigwords": [],
        "crwords": [
            "posture corrector",
            "posture correcteur dos",
            "maintien dos",
            "ceinture pour le dos",
            "posture pro",
            "mal de dos",
            "tshirt redresseur de dos",
            "truefit posture corrector",
            "ceinture dorsale",
            "perko dos femme",
            "ceinture maintien dos"
        ],
        "broader_words": [],
        "negative_words": [
            "appareil massage dos"
        ],
        "bigwords_rank": [],
        "crwords_rank": {
            "posture corrector": 98738,
            "posture correcteur dos": 16374,
            "maintien dos": 38123,
            "ceinture pour le dos": 40297,
            "posture pro": 42183,
            "mal de dos": 48952,
            "tshirt redresseur de dos": 44791,
            "truefit posture corrector": 61866,
            "ceinture dorsale": 65019,
            "perko dos femme": 71083,
            "ceinture maintien dos": 81423
        },
        "cost": 91.4705590903759
    }
}

save_keywords_to_excel(result)
