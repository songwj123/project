import pandas as pd


def save_keywords_to_excel(result, file_name="11111.xlsx"):
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
            "sleep mask",
            "eye mask",
            "eye massager",
            "fsa eligible items only list",
            "eye care",
            "renpho eye massager",
            "heated eye mask",
            "sleep mask with bluetooth headphones",
            "face care",
            "bluetooth sleep mask",
            "head massager scalp stress relax",
            "eye mask sleep",
            "eye health",
            "eye mask massager",
            "therabody eye goggles",
            "eyeris 3 eye massager",
            "heated eye massager",
            "eye massage",
            "smart goggles",
            "massaging eye mask",
            "bluetooth eye mask",
            "eye massager with heat",
            "migraine eye mask",
            "migraine massager",
            "sinus massager",
            "migraine eye massager",
            "therabody smart goggles",
            "temple massager",
            "eye massager with heat renpho",
            "eye massage mask",
            "eye strain",
            "heat massager",
            "face massager mask",
            "smart sleep mask",
            "migraine relief massager",
            "masajeador de ojos",
            "eye mask massager with heat",
            "sinus massager with heat",
            "massage mask",
            "eye massager with cooling",
            "serenity tension relief pro migraine",
            "headache massager for migraines",
            "migraine relief gadget"
        ],
        "broader_words": [],
        "negative_words": [
            "renpho eyeris 3",
            "sleep mask men",
            "renpho eyeris 1"
        ],
        "bigwords_rank": {},
        "crwords_rank": {
            "sleep mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 555
            },
            "eye mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1018
            },
            "eye massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 14274
            },
            "fsa eligible items only list": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 3409
            },
            "eye care": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 16357
            },
            "renpho eye massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 38874
            },
            "heated eye mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 29483
            },
            "sleep mask with bluetooth headphones": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 43135
            },
            "face care": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 66120
            },
            "bluetooth sleep mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 67062
            },
            "head massager scalp stress relax": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 102980
            },
            "eye mask sleep": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 180678
            },
            "eye health": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 270665
            },
            "eye mask massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 375905
            },
            "therabody eye goggles": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 441025
            },
            "eyeris 3 eye massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 469619
            },
            "heated eye massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 480118
            },
            "eye massage": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 487249
            },
            "renpho eyeris 3": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 518533
            },
            "smart goggles": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 535925
            },
            "massaging eye mask": {
                "src": "null",
                "rank": 564084
            },
            "bluetooth eye mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 606119
            },
            "eye massager with heat": {
                "src": "null",
                "rank": 611855
            },
            "migraine eye mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 705315
            },
            "migraine massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 800966
            },
            "sleep mask men": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 810764
            },
            "sinus massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 912286
            },
            "migraine eye massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 938500
            },
            "therabody smart goggles": {
                "src": "null",
                "rank": 1112736
            },
            "temple massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1151750
            },
            "eye massager with heat renpho": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1172379
            },
            "eye massage mask": {
                "src": "null",
                "rank": 1237887
            },
            "eye strain": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1632429
            },
            "heat massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1715421
            },
            "face massager mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1715421
            },
            "smart sleep mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1715421
            },
            "migraine relief massager": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1857948
            },
            "masajeador de ojos": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1965803
            },
            "eye mask massager with heat": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 2086842
            },
            "sinus massager with heat": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 2152601
            },
            "massage mask": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 2374659
            },
            "eye massager with cooling": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 2458639
            },
            "serenity tension relief pro migraine": {
                "src": [
                    "145w"
                ],
                "rank": 450310
            },
            "renpho eyeris 1": {
                "src": [
                    "145w"
                ],
                "rank": 1076322
            },
            "headache massager for migraines": {
                "src": [
                    "145w"
                ],
                "rank": 1131870
            },
            "migraine relief gadget": {
                "src": [
                    "145w"
                ],
                "rank": 1337327
            }
        }
    }
}

save_keywords_to_excel(result)
