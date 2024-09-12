import pandas as pd


def save_keywords_to_excel(result, file_name="B0BHRZBHNX.xlsx"):
    data = {
        "Bid Words": result.get('bidwords', []),
        "CR Words": result.get('crwords', []),
        "Broader Words": result.get('broader_words', []),
        "Negative Words": result.get('negative_words', [])
    }

    with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
        for sheet_name, keywords in data.items():
            df = pd.DataFrame(keywords, columns=[sheet_name])

            # Write each DataFrame to a different sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Data successfully saved to {file_name}")


result = {'bidwords': ['lap desk', 'laptop stand for bed', 'laptop desk', 'folding desk', 'floor desk', 'bed desk',
                       'laptop table', 'laptop lap desk', 'lap table', 'lap desk for laptop with cushion',
                       'laptop bed tray'],
          'crwords': ['apartment desk', 'work lap table', '25 inch desk', 'wall desk fold down for small spaces',
                      'tray table lap desk', 'laptop bed tray', 'portable lap desk table', 'lap desk with mouse pad',
                      'foldable desk', 'bed lap desk', 'folding laptop desk', 'portable lap desk laptop',
                      'foldable bed lap desk', 'lap tables for adults', 'laptop table for bed',
                      'portable folding laptop desk', 'folding lap desks kids', 'foldable floor table',
                      'wood folding desk', 'lap desk with ventilation', 'reading lap desk', 'laptop foldable desk',
                      'foldable laptop desk', 'lap desk', 'wide foldable laptop desk', 'lap laptop desk 17 inch',
                      'lap desk with cup holder', 'folding lap desks adults', 'lap desk cushion',
                      'portable desk for bed', 'laptop lap desk', 'adjustable laptop lap desk', 'portable lap desk',
                      'raised lap desk', 'lap top bed tray desk', 'laptop tray for couch',
                      'foldable large laptop lap desk', 'collapsible desk for small spaces', 'bed laptop table',
                      'folding lap tv tray', 'lap table for couch', 'sofa lap desk', 'lap desk folding chair',
                      'adjustable lap desk', 'lap board', 'folding computer table', 'laptop lap table',
                      'folding lap desk 23.6 inch', 'laptop foldable tray', 'lap desk with sides',
                      'multi media lap desk', 'extra wide lap desk', 'foldable desk table', 'laptop lap desk 17in',
                      'folding table lap', 'laptop lap stand', 'table bed', 'lap desk couch', 'lap laptop desk',
                      'white folding desk', 'desk tray lap', 'lap desk foldable', 'lap desk 17 inch laptop',
                      'computer bed tray for laptop', 'lapdesk for laptop', 'folding lap desk 23.6', 'large lap desk',
                      'lap desk bed table', 'lap top desk tray', 'folding laptop desk bed', 'small laptop desk',
                      'computer tray for bed', 'bed table', 'lap stand desk', 'fisyod foldable laptop desk',
                      'folding desk', 'foldable desk laptop table', 'folding desk chair for small space',
                      'folding standing laptop desk', 'bed tray for laptop', 'folding desks for small spaces',
                      'wood lap desk', 'collapsible laptop lap desk', 'lap desk pc', 'desk lap', 'folded laptop desk',
                      'computer stand for bed', 'floor lap desk', 'space saver desk', 'laptop lap desk wood',
                      'foldable usb lap desk', 'lap desk with stand', 'lap desk for bed', 'buyify folding lap desk',
                      'laptop stand for bed', 'no assembly desk', 'folding computer desk', 'foldable computer desk',
                      'fold up desks for small spaces', 'portable folding desk', 'lap deak', 'folding writing desk',
                      'folding laptop', 'folding office desk', 'folding lap desk bed', 'folding lap desk with light',
                      'lap desk with tray', 'folding lap desk', 'folding lap computer desk', 'writing lap desk',
                      'lap top tray for lap', 'fold down desk', 'foldable sitting desk',
                      'laptop pillow lap desk for bed', 'foldable computer desk bed', 'travel desk', 'pink lap desk',
                      'portable lap desk bed table', 'lap desk with storage', 'folding working desk',
                      'folding sofa desk', 'folding table laptop', 'lap desk with cushion', 'lapdesk with cushion',
                      'lap homework desk', 'folding lap top desk', 'home office lap desks', 'lapdesk folding',
                      'lap table', 'laptop lap tray', 'computer lap desk laptop', 'wall mounted desk folding',
                      'laptop lap desk folding', 'fold away desk', 'laptop cushion for lap', 'folding couch desk',
                      'portable folding lap desk', 'folding desk bed', 'bed desk foldable', 'fold laptop table',
                      'lap desk with legs', 'wooden lap desk', 'black folding desk', 'foldable lap deak',
                      'lap desk laptop', 'foldable keyboard desk', 'computer lap desk', 'lap desk bed', 'lap tray',
                      'computer tray', 'easy assemble desk', 'foldable laptop desk with storage',
                      'foldable lap top desk', 'lap tray for laptop', 'foldable study table', 'small lap desk',
                      'lap table for laptop', 'lap desks for laptops', 'lap desk with light', 'lap folding tray',
                      'study table for bed', 'escritorio plegable', 'lap desks for adults', 'desk table lap',
                      'sitting desk', 'small folding desk', 'laptop tray for lap', 'folding floor desk', 'lap desks',
                      'bed work table for laptop', 'foldable lap desk', 'pillow lap desk', '23.6 lap desk',
                      'collapsible desk', 'desktop lap table', 'lapdesk', 'work desk for bed', 'origami desk',
                      'floor foldable desk', 'lap table for bed', 'laptop desk for lap', 'amazon lap desks',
                      'lap desk for car', 'bed desk table', 'fold up desk', 'folding lap desk laptop',
                      'bed computer table for laptop', 'computer lap tray', 'laptop tray'],
          'broader_words': ['lap table', 'laptop desk', 'laptop table', 'bed desk', 'laptop bed tray', 'floor desk'],
          'negative_words': ['black kitchen', 'mini talbe', 'kitchen movie', 'bes sesk', 'mesa para comer en cama',
                             'college students', 'bed trays eating kids', 'child tv trays eating',
                             'kids dinner trays eating', 'reading cup'],
          'bigwords_rank': [2608, 20444, -1, 15715, -1, -1, -1, 27610, -1, 26259, -1],
          'crwords_rank': [821149, -1, 1112736, 198961, -1, 187971, -1, 729306, -1, 938500, 1193496, -1, -1, 153541,
                           76772, -1, -1, 899706, -1, -1, -1, -1, 435059, 2608, -1, -1, 763648, -1, 1193496, 912286,
                           27610, -1, 378196, -1, -1, 402171, -1, 642496, -1, -1, 1112736, -1, -1, 215093, 579229,
                           951965, 1042132, -1, -1, -1, -1, 1151750, 589722, -1, -1, 476569, 606119, -1, 522774,
                           1094316, -1, -1, 887533, 912286, 228739, -1, 327246, -1, -1, -1, 296425, 564084, -1, -1, -1,
                           15715, -1, 1094316, -1, 435059, 103355, -1, -1, -1, 1112736, -1, 506268, -1, 1131870, -1, -1,
                           -1, 255004, -1, 20444, 423506, 251809, 288224, 810764, -1, 1010303, -1, -1, 1042132, -1, -1,
                           -1, 369205, -1, -1, 510243, 288224, -1, 589722, -1, 394655, 995104, -1, 323800, -1, -1, -1,
                           173361, 450310, -1, -1, -1, -1, 61402, 273001, -1, 925162, -1, 746238, 518533, -1, -1, -1,
                           -1, -1, 1112736, 1172379, -1, -1, -1, -1, 151236, -1, 59511, 1010303, 1151750, -1, -1,
                           629853, 781879, 1151750, 344917, 1112736, 629853, -1, 754863, 912286, 42453, -1, 1131870,
                           122606, 642496, -1, 92872, 1112736, 309516, 938500, -1, 167067, -1, 69736, 1172379, 1193496,
                           -1, 853035, 222904, 1042132, 600517, 373610, 264788, -1, 404691, 853035, 92012]}

save_keywords_to_excel(result)
