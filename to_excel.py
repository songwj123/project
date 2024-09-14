import pandas as pd


def save_keywords_to_excel(result, file_name="B08TV7KP8V.xlsx"):
    bigwords = result['data'].get('bigwords', [])
    crwords = result['data'].get('crwords', [])
    broader_words = result['data'].get('broader_words', [])
    negative_words = result['data'].get('negative_words', [])
    crwords_rank = result['data'].get('crwords_rank', {})

    def get_rank_data(words, rank_data):
        data = []
        for word in words:
            rank_info = rank_data.get(word, {})
            src = ', '.join(rank_info.get('src', [])) if rank_info.get('src') else 'null'
            rank = rank_info.get('rank', None)
            data.append({'高转化词': word, '来源': src, '排名': rank})
        return data

    bigwords_data = [{'大词': word, '来源': 'null', '排名': rank} for word, rank in
                     zip(bigwords, result['data'].get('bigwords_rank', [None]))]
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


result ={'code': 0, 'msg': 'success', 'data': {'bigwords': [], 'crwords': ['plant light', 'grow light', 'led grow light', 'plant grow light', 'indoor plant light', 'full spectrum grow light', 'grow lamp', 'plant lamp', 'plant growing lamps', 'full spectrum led grow light', 'grow light stand', 'indoor plant grow light', 'growing light', 'grow light lamp', 'small plant light', 'standing grow light', 'indoor grow light', 'led grow light bulb', 'tall grow light', 'plant growing light', 'standing plant light', 'grow light with stand', 'large grow light', 'plant light with timer', 'full spectrum plant light', 'plant grow lamp', '300 watt grow light', '6500k led grow light', 'solar grow light', 'floor grow light', '100w led grow light', '400 watt grow light', 'plant led light', 'grow lights for cannabis', 'uv plant lights for indoor growing', 'canabis grow light', 'cannabis grow light', 'cactus grow light', 'grow light for cannabis', 'led grow lights full spectrum', 'lbw grow light for indoor plants'], 'broader_words': [], 'negative_words': [], 'bigwords_rank': [], 'crwords_rank': {'plant light': {'src': ['v3'], 'rank': 17979}, 'grow light': {'src': ['v2', 'v3'], 'rank': 7315}, 'led grow light': {'src': ['v2', 'v3'], 'rank': 44217}, 'plant grow light': {'src': ['v3'], 'rank': 65024}, 'indoor plant light': {'src': ['v3'], 'rank': 75910}, 'full spectrum grow light': {'src': ['v3'], 'rank': 78418}, 'grow lamp': {'src': ['v2', 'v3'], 'rank': 187971}, 'plant lamp': {'src': ['v3'], 'rank': 222904}, 'plant growing lamps': {'src': ['v2', 'v3'], 'rank': 227029}, 'full spectrum led grow light': {'src': ['v2', 'v3'], 'rank': 244849}, 'grow light stand': {'src': None, 'rank': 238425}, 'indoor plant grow light': {'src': ['v2', 'v3'], 'rank': 303562}, 'growing light': {'src': None, 'rank': 429235}, 'grow light lamp': {'src': ['v2', 'v3'], 'rank': 459849}, 'small plant light': {'src': ['v3'], 'rank': 487249}, 'standing grow light': {'src': ['v3'], 'rank': 522774}, 'indoor grow light': {'src': ['v2', 'v3'], 'rank': 564084}, 'led grow light bulb': {'src': ['v2'], 'rank': 682958}, 'tall grow light': {'src': ['v3'], 'rank': 899706}, 'plant growing light': {'src': ['v2', 'v3'], 'rank': 995104}, 'standing plant light': {'src': ['v3'], 'rank': 1010303}, 'grow light with stand': {'src': None, 'rank': 1094316}, 'large grow light': {'src': ['v2'], 'rank': 1131870}, 'plant light with timer': {'src': None, 'rank': 1151750}, 'full spectrum plant light': {'src': ['v3'], 'rank': 1632429}, 'plant grow lamp': {'src': ['v2'], 'rank': 1632429}, '300 watt grow light': {'src': ['v2', 'v3'], 'rank': 1965803}, '6500k led grow light': {'src': ['v2'], 'rank': 1965803}, 'solar grow light': {'src': ['v2'], 'rank': 2024633}, 'floor grow light': {'src': ['v3'], 'rank': 2086842}, '100w led grow light': {'src': ['v2'], 'rank': 2152601}, '400 watt grow light': {'src': ['v2'], 'rank': 2152601}, 'plant led light': {'src': ['v3'], 'rank': 2152601}, 'grow lights for cannabis': {'src': ['145w'], 'rank': 221312}, 'uv plant lights for indoor growing': {'src': ['145w'], 'rank': 690305}, 'canabis grow light': {'src': ['145w'], 'rank': 705315}, 'cannabis grow light': {'src': ['145w'], 'rank': 875628}, 'cactus grow light': {'src': ['145w'], 'rank': 951965}, 'grow light for cannabis': {'src': ['145w'], 'rank': 1059020}, 'led grow lights full spectrum': {'src': ['145w'], 'rank': 1151750}, 'lbw grow light for indoor plants': {'src': ['145w'], 'rank': 1364851}}}}


save_keywords_to_excel(result)
