import pandas as pd

# 数据
data = {
    "code": 0,
    "msg": "success",
    "data": {
        "bigwords": [
            "flawless facial hair remover",
            "facial hair removal for women",
            "hair removal device",
            "face shaver for women",
            "flawless",
            "hair removal",
            "finishing touch flawless",
            "face shaver",
            "face hair removal for women",
            "facial hair remover for women face"
        ],
        "crwords": [
            "bikini trimmer",
            "facial hair remover",
            "hair remover",
            "womens face razor peach fuzz",
            "upper lip hair removal",
            "womens facial hair shaver",
            "face epilator",
            "flawless hair remover",
            "facial hair trimmer",
            "depiladora facial para mujer",
            "women facial hair remover",
            "facial hair removal",
            "face hair remover",
            "plucy facial hair remover",
            "face hair removal",
            "hero epilator facial hair removal",
            "face hair trimmer women",
            "women face shaver peach fuzz",
            "facial trimmer",
            "ladies facial hair shaver",
            "facial hair removal device",
            "flawless face hair remover",
            "plucky facial hair removal",
            "face hair trimmer",
            "heroepilator facial hair remover",
            "women facial hair trimmer",
            "upper lip hair remover",
            "female face shaver",
            "face hair removal device",
            "womens facial hair remover device",
            "lip shaver",
            "female face shaver peach fuzz",
            "women facial hair removal device",
            "facial hair shaver",
            "flawless rechargeable facial hair remover",
            "eyebrow epilator",
            "womens lip shaver",
            "electric facial razor",
            "facial hair trimmer women",
            "face nair hair remover",
            "finishing touch flawless facial hair remover",
            "womens facial hair remover",
            "finishing touch",
            "hair remover for face woman",
            "womens face shavers",
            "peach fuzz remover for women face",
            "chin hair removal for women",
            "face trimmer for women",
            "facial hair trimmer for women",
            "women shavers",
            "electric face shaver",
            "epilators hair removal for women face",
            "hair removal for women",
            "hair remover for women",
            "face epilator for women",
            "womens facial hair removal devices",
            "women face shaver",
            "electric face shaver for women",
            "women's facial hair remover",
            "razors for women face hair",
            "womens shavers for facial hair",
            "facial shaver for women",
            "womens face razor",
            "personal shaver for women",
            "face shaver for women facial hair",
            "women shaver",
            "lip hair removal for women",
            "women's shaver",
            "glabrousskin hair remover for face",
            "womens razors for shaving face",
            "women's face shaver",
            "womens hair removal for face",
            "womens face razors for facial hair",
            "shaver for women face hair",
            "womens facial razor",
            "womens face shaver",
            "women's shaving & hair removal products",
            "chin hair removal permanent",
            "mustache trimmer women",
            "afeitadora para mujer",
            "mustache remover women",
            "flawless facial hair remover replacement heads",
            "facial trimmer for women",
            "face razors for women electric",
            "electric hair remover for women",
            "flawless razor",
            "womens electric razor for face",
            "peach fuzz remover",
            "chin hair remover for women face",
            "electric razors for women face",
            "face shaver women",
            "ladies face shaver for peach fuzz",
            "ladies razors for facial hair",
            "womens face shaver peach fuzz",
            "flawless hair removal",
            "women's facial hair shaver",
            "painless hair removal for women",
            "facial hair remover for women",
            "braun facial hair removal for women",
            "hair removal device for women",
            "facial shaver",
            "lip shaver for women facial hair",
            "flawless face",
            "ladies shaver",
            "glamorous skin",
            "upper lip hair removal for women",
            "ladies shavers for facial hair",
            "face razor for women facial hair",
            "hair shaver for women",
            "facial hair removal for women face",
            "electric facial hair remover for women",
            "ladies face shaver",
            "women's face razor",
            "flawless hair remover for face",
            "woman face shaver",
            "flawless shaver",
            "peach fuzz remover for women",
            "electric tweezers",
            "electric tweezers for women facial hair",
            "epilator for women facial hair removal",
            "womens facial hair trimmer",
            "flawless finishing touch",
            "women hair removal",
            "female facial hair remover",
            "glabours skin hair remover for women",
            "hair face removal for women",
            "facial hair razor",
            "epilator face",
            "best facial hair remover for women",
            "ladies facial hair remover",
            "womens face hair remover",
            "best face razors for women",
            "painless hair removal",
            "women's razors electric",
            "best face hair remover for women",
            "razor for women face",
            "hair removal for face",
            "electric face razors for women",
            "mustache shavers for women",
            "braun face mini hair remover",
            "best face shaver for women",
            "flawless razors for women",
            "womens mustache hair remover",
            "electric shaver for women face",
            "womens facial razors for peach fuzz",
            "womens mustache shaver",
            "face trimmer for women facial hair",
            "mini shaver for women",
            "no no hair remover for women",
            "women shavers for face",
            "face hair remover for women",
            "face razor for women",
            "facial razors for women",
            "electric razor for women face",
            "women face hair removal",
            "facial hair",
            "hair removal tool",
            "mustache razors for women",
            "hair removal face",
            "glamorous skin hair remover",
            "woman facial hair remover",
            "conture hair removal tool",
            "women's face shaver for peach fuzz",
            "womens facial shaver",
            "hair removal device for face",
            "gurelax facial hair removal for women",
            "hair epilators, groomers & trimmers",
            "electric hair remover",
            "women facial razor",
            "micro razors for women face",
            "womens facial hair removal",
            "chin hair removal",
            "remove facial hair on women face",
            "mustache shaver",
            "women hair removal device",
            "women razors for shaving face",
            "women's facial shaver",
            "depiladora de bigote para mujer"
        ],
        "broader_words": [
            "flawless facial hair remover",
            "facial hair removal for women",
            "hair removal device",
            "face shaver for women",
            "flawless",
            "hair removal",
            "finishing touch flawless",
            "face shaver",
            "face hair removal for women",
            "facial hair remover for women face"
        ],
        "negative_words": [
            "flamingo facial hair remover"
        ],
        "bigwords_rank": {
            "flawless facial hair remover": 4517,
            "facial hair removal for women": 4858,
            "hair removal device": 12984,
            "face shaver for women": 13852,
            "flawless": 20635,
            "hair removal": 21831,
            "finishing touch flawless": 35304,
            "face shaver": 37663,
            "face hair removal for women": 46841,
            "facial hair remover for women face": 49221
        },
        "crwords_rank": {
            "hair removal device": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 12984
            },
            "flawless facial hair remover": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 4517
            },
            "hair removal": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 21831
            },
            "bikini trimmer": {
                "src": [
                    "v3"
                ],
                "rank": 31972
            },
            "face shaver": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 37663
            },
            "facial hair remover": {
                "src": None,
                "rank": 66713
            },
            "hair remover": {
                "src": None,
                "rank": 58696
            },
            "womens face razor peach fuzz": {
                "src": None,
                "rank": 85791
            },
            "upper lip hair removal": {
                "src": None,
                "rank": 128014
            },
            "womens facial hair shaver": {
                "src": None,
                "rank": 135058
            },
            "face epilator": {
                "src": None,
                "rank": 138347
            },
            "flawless hair remover": {
                "src": None,
                "rank": 138347
            },
            "facial hair trimmer": {
                "src": None,
                "rank": 140057
            },
            "depiladora facial para mujer": {
                "src": None,
                "rank": 171877
            },
            "women facial hair remover": {
                "src": None,
                "rank": 202277
            },
            "facial hair removal": {
                "src": None,
                "rank": 205014
            },
            "face hair remover": {
                "src": None,
                "rank": 280413
            },
            "plucy facial hair remover": {
                "src": None,
                "rank": 364961
            },
            "face hair removal": {
                "src": None,
                "rank": 399632
            },
            "hero epilator facial hair removal": {
                "src": [
                    "v2"
                ],
                "rank": 426313
            },
            "face hair trimmer women": {
                "src": None,
                "rank": 441025
            },
            "women face shaver peach fuzz": {
                "src": None,
                "rank": 459849
            },
            "facial trimmer": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 675892
            },
            "ladies facial hair shaver": {
                "src": None,
                "rank": 675892
            },
            "facial hair removal device": {
                "src": None,
                "rank": 791153
            },
            "flawless face hair remover": {
                "src": None,
                "rank": 864211
            },
            "plucky facial hair removal": {
                "src": None,
                "rank": 864211
            },
            "face hair trimmer": {
                "src": None,
                "rank": 887533
            },
            "heroepilator facial hair remover": {
                "src": None,
                "rank": 995104
            },
            "women facial hair trimmer": {
                "src": None,
                "rank": 1112736
            },
            "upper lip hair remover": {
                "src": None,
                "rank": 1151750
            },
            "female face shaver": {
                "src": None,
                "rank": 1237887
            },
            "face hair removal device": {
                "src": None,
                "rank": 1311011
            },
            "womens facial hair remover device": {
                "src": None,
                "rank": 1285581
            },
            "lip shaver": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1520933
            },
            "female face shaver peach fuzz": {
                "src": [
                    "v2"
                ],
                "rank": 1632429
            },
            "women facial hair removal device": {
                "src": [
                    "v2"
                ],
                "rank": 1632429
            },
            "facial hair shaver": {
                "src": [
                    "v2"
                ],
                "rank": 1673056
            },
            "flawless rechargeable facial hair remover": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 1715421
            },
            "eyebrow epilator": {
                "src": [
                    "v2"
                ],
                "rank": 2024633
            },
            "womens lip shaver": {
                "src": [
                    "v2",
                    "v3"
                ],
                "rank": 2152601
            },
            "electric facial razor": {
                "src": [
                    "v2"
                ],
                "rank": 2221966
            },
            "facial hair trimmer women": {
                "src": [
                    "v3"
                ],
                "rank": 2221966
            },
            "flamingo facial hair remover": {
                "src": [
                    "v2"
                ],
                "rank": 2295805
            },
            "face nair hair remover": {
                "src": [
                    "v2"
                ],
                "rank": 2374659
            },
            "finishing touch flawless facial hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 53680
            },
            "womens facial hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 69840
            },
            "finishing touch": {
                "src": [
                    "145w"
                ],
                "rank": 82636
            },
            "hair remover for face woman": {
                "src": [
                    "145w"
                ],
                "rank": 100780
            },
            "womens face shavers": {
                "src": [
                    "145w"
                ],
                "rank": 121847
            },
            "peach fuzz remover for women face": {
                "src": [
                    "145w"
                ],
                "rank": 126652
            },
            "chin hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 154692
            },
            "face trimmer for women": {
                "src": [
                    "145w"
                ],
                "rank": 167988
            },
            "facial hair trimmer for women": {
                "src": [
                    "145w"
                ],
                "rank": 173872
            },
            "women shavers": {
                "src": [
                    "145w"
                ],
                "rank": 206365
            },
            "electric face shaver": {
                "src": [
                    "145w"
                ],
                "rank": 226169
            },
            "epilators hair removal for women face": {
                "src": [
                    "145w"
                ],
                "rank": 229565
            },
            "hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 231290
            },
            "hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 237514
            },
            "face epilator for women": {
                "src": [
                    "145w"
                ],
                "rank": 241100
            },
            "womens facial hair removal devices": {
                "src": [
                    "145w"
                ],
                "rank": 255004
            },
            "women face shaver": {
                "src": [
                    "145w"
                ],
                "rank": 264788
            },
            "electric face shaver for women": {
                "src": [
                    "145w"
                ],
                "rank": 271832
            },
            "women's facial hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 271832
            },
            "razors for women face hair": {
                "src": [
                    "145w"
                ],
                "rank": 276680
            },
            "womens shavers for facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 276680
            },
            "facial shaver for women": {
                "src": [
                    "145w"
                ],
                "rank": 277875
            },
            "womens face razor": {
                "src": [
                    "145w"
                ],
                "rank": 282923
            },
            "personal shaver for women": {
                "src": [
                    "145w"
                ],
                "rank": 295050
            },
            "face shaver for women facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 299230
            },
            "women shaver": {
                "src": [
                    "145w"
                ],
                "rank": 305050
            },
            "lip hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 305050
            },
            "women's shaver": {
                "src": [
                    "145w"
                ],
                "rank": 322131
            },
            "glabrousskin hair remover for face": {
                "src": [
                    "145w"
                ],
                "rank": 323800
            },
            "womens razors for shaving face": {
                "src": [
                    "145w"
                ],
                "rank": 327246
            },
            "women's face shaver": {
                "src": [
                    "145w"
                ],
                "rank": 330706
            },
            "womens hair removal for face": {
                "src": [
                    "145w"
                ],
                "rank": 352648
            },
            "womens face razors for facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 369205
            },
            "shaver for women face hair": {
                "src": [
                    "145w"
                ],
                "rank": 387509
            },
            "womens facial razor": {
                "src": [
                    "145w"
                ],
                "rank": 402171
            },
            "womens face shaver": {
                "src": [
                    "145w"
                ],
                "rank": 407286
            },
            "women's shaving & hair removal products": {
                "src": [
                    "145w"
                ],
                "rank": 412614
            },
            "chin hair removal permanent": {
                "src": [
                    "145w"
                ],
                "rank": 415264
            },
            "mustache trimmer women": {
                "src": [
                    "145w"
                ],
                "rank": 417993
            },
            "afeitadora para mujer": {
                "src": [
                    "145w"
                ],
                "rank": 423506
            },
            "mustache remover women": {
                "src": [
                    "145w"
                ],
                "rank": 435059
            },
            "flawless facial hair remover replacement heads": {
                "src": [
                    "145w"
                ],
                "rank": 453431
            },
            "facial trimmer for women": {
                "src": [
                    "145w"
                ],
                "rank": 473036
            },
            "face razors for women electric": {
                "src": [
                    "145w"
                ],
                "rank": 502304
            },
            "electric hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 510243
            },
            "flawless razor": {
                "src": [
                    "145w"
                ],
                "rank": 522774
            },
            "womens electric razor for face": {
                "src": [
                    "145w"
                ],
                "rank": 531479
            },
            "peach fuzz remover": {
                "src": [
                    "145w"
                ],
                "rank": 535925
            },
            "chin hair remover for women face": {
                "src": [
                    "145w"
                ],
                "rank": 544912
            },
            "electric razors for women face": {
                "src": [
                    "145w"
                ],
                "rank": 554371
            },
            "face shaver women": {
                "src": [
                    "145w"
                ],
                "rank": 589722
            },
            "ladies face shaver for peach fuzz": {
                "src": [
                    "145w"
                ],
                "rank": 600517
            },
            "ladies razors for facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 606119
            },
            "womens face shaver peach fuzz": {
                "src": [
                    "145w"
                ],
                "rank": 611855
            },
            "flawless hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 623612
            },
            "women's facial hair shaver": {
                "src": [
                    "145w"
                ],
                "rank": 629853
            },
            "painless hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 636131
            },
            "facial hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 668965
            },
            "braun facial hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 675892
            },
            "hair removal device for women": {
                "src": [
                    "145w"
                ],
                "rank": 675892
            },
            "facial shaver": {
                "src": [
                    "145w"
                ],
                "rank": 690305
            },
            "lip shaver for women facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 705315
            },
            "flawless face": {
                "src": [
                    "145w"
                ],
                "rank": 705315
            },
            "ladies shaver": {
                "src": [
                    "145w"
                ],
                "rank": 713245
            },
            "glamorous skin": {
                "src": [
                    "145w"
                ],
                "rank": 721280
            },
            "upper lip hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 729306
            },
            "ladies shavers for facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 772610
            },
            "face razor for women facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 772610
            },
            "hair shaver for women": {
                "src": [
                    "145w"
                ],
                "rank": 781879
            },
            "facial hair removal for women face": {
                "src": [
                    "145w"
                ],
                "rank": 781879
            },
            "electric facial hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 791153
            },
            "ladies face shaver": {
                "src": [
                    "145w"
                ],
                "rank": 791153
            },
            "women's face razor": {
                "src": [
                    "145w"
                ],
                "rank": 810764
            },
            "flawless hair remover for face": {
                "src": [
                    "145w"
                ],
                "rank": 821149
            },
            "woman face shaver": {
                "src": [
                    "145w"
                ],
                "rank": 821149
            },
            "flawless shaver": {
                "src": [
                    "145w"
                ],
                "rank": 831436
            },
            "peach fuzz remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 831436
            },
            "electric tweezers": {
                "src": [
                    "145w"
                ],
                "rank": 831436
            },
            "electric tweezers for women facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 831436
            },
            "epilator for women facial hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 831436
            },
            "womens facial hair trimmer": {
                "src": [
                    "145w"
                ],
                "rank": 831436
            },
            "flawless finishing touch": {
                "src": [
                    "145w"
                ],
                "rank": 864211
            },
            "women hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 864211
            },
            "female facial hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 864211
            },
            "glabours skin hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 864211
            },
            "hair face removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 875628
            },
            "facial hair razor": {
                "src": [
                    "145w"
                ],
                "rank": 899706
            },
            "epilator face": {
                "src": [
                    "145w"
                ],
                "rank": 912286
            },
            "best facial hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 925162
            },
            "ladies facial hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 925162
            },
            "womens face hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 925162
            },
            "best face razors for women": {
                "src": [
                    "145w"
                ],
                "rank": 938500
            },
            "painless hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 938500
            },
            "women's razors electric": {
                "src": [
                    "145w"
                ],
                "rank": 938500
            },
            "best face hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 951965
            },
            "razor for women face": {
                "src": [
                    "145w"
                ],
                "rank": 951965
            },
            "hair removal for face": {
                "src": [
                    "145w"
                ],
                "rank": 965759
            },
            "electric face razors for women": {
                "src": [
                    "145w"
                ],
                "rank": 965759
            },
            "mustache shavers for women": {
                "src": [
                    "145w"
                ],
                "rank": 980129
            },
            "braun face mini hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 995104
            },
            "best face shaver for women": {
                "src": [
                    "145w"
                ],
                "rank": 1026064
            },
            "flawless razors for women": {
                "src": [
                    "145w"
                ],
                "rank": 1026064
            },
            "womens mustache hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 1042132
            },
            "electric shaver for women face": {
                "src": [
                    "145w"
                ],
                "rank": 1059020
            },
            "womens facial razors for peach fuzz": {
                "src": [
                    "145w"
                ],
                "rank": 1059020
            },
            "womens mustache shaver": {
                "src": [
                    "145w"
                ],
                "rank": 1059020
            },
            "face trimmer for women facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 1076322
            },
            "mini shaver for women": {
                "src": [
                    "145w"
                ],
                "rank": 1094316
            },
            "no no hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 1094316
            },
            "women shavers for face": {
                "src": [
                    "145w"
                ],
                "rank": 1131870
            },
            "face hair remover for women": {
                "src": [
                    "145w"
                ],
                "rank": 1172379
            },
            "face razor for women": {
                "src": [
                    "145w"
                ],
                "rank": 1172379
            },
            "facial razors for women": {
                "src": [
                    "145w"
                ],
                "rank": 1172379
            },
            "electric razor for women face": {
                "src": [
                    "145w"
                ],
                "rank": 1237887
            },
            "women face hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 1237887
            },
            "facial hair": {
                "src": [
                    "145w"
                ],
                "rank": 1237887
            },
            "hair removal tool": {
                "src": [
                    "145w"
                ],
                "rank": 1261277
            },
            "mustache razors for women": {
                "src": [
                    "145w"
                ],
                "rank": 1311011
            },
            "hair removal face": {
                "src": [
                    "145w"
                ],
                "rank": 1311011
            },
            "glamorous skin hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 1337327
            },
            "woman facial hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 1364851
            },
            "conture hair removal tool": {
                "src": [
                    "145w"
                ],
                "rank": 1364851
            },
            "women's face shaver for peach fuzz": {
                "src": [
                    "145w"
                ],
                "rank": 1364851
            },
            "womens facial shaver": {
                "src": [
                    "145w"
                ],
                "rank": 1364851
            },
            "hair removal device for face": {
                "src": [
                    "145w"
                ],
                "rank": 1364851
            },
            "gurelax facial hair removal for women": {
                "src": [
                    "145w"
                ],
                "rank": 1364851
            },
            "hair epilators, groomers & trimmers": {
                "src": [
                    "145w"
                ],
                "rank": 1393520
            },
            "electric hair remover": {
                "src": [
                    "145w"
                ],
                "rank": 1393520
            },
            "women facial razor": {
                "src": [
                    "145w"
                ],
                "rank": 1393520
            },
            "micro razors for women face": {
                "src": [
                    "145w"
                ],
                "rank": 1423306
            },
            "womens facial hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 1423306
            },
            "chin hair removal": {
                "src": [
                    "145w"
                ],
                "rank": 1423306
            },
            "remove facial hair on women face": {
                "src": [
                    "145w"
                ],
                "rank": 1454271
            },
            "mustache shaver": {
                "src": [
                    "145w"
                ],
                "rank": 1486915
            },
            "women hair removal device": {
                "src": [
                    "145w"
                ],
                "rank": 1486915
            },
            "women razors for shaving face": {
                "src": [
                    "145w"
                ],
                "rank": 1486915
            },
            "women's facial shaver": {
                "src": [
                    "145w"
                ],
                "rank": 1486915
            },
            "depiladora de bigote para mujer": {
                "src": [
                    "145w"
                ],
                "rank": 1486915
            }
        }
    }
}
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
output_file = "cs-1015.xlsx"
# df.to_excel(output_file, index=False)

# print(f"Data saved to {output_file}")

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for sheet_name, keywords in data.items():
        df = pd.DataFrame(keywords)
        df.to_excel(writer, sheet_name=sheet_name, index=True)
