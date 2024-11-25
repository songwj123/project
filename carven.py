'''
"users_count": 总用户数量,
"companies_count": 总公司数量
"shop_count": 总店铺数量
"ads_count": 自动化广告总数量
'''
@api.route('/advertising_statistics', methods=['GET'])
def advertising_statistics_view():
    """
    广告数据统计接口，返回广告数据统计信息。
    """
    advertis_statistics = data_statistic_services.advertising_statistics()
    return success_response(data={"data": advertis_statistics})

def advertising_statistics():
    user_count = SysUser.query.count()
    company_count = SysCompany.query.count()
    shop_count = AmazonAdProfiles.query.count()
    ads_count = SysAdAutoInfo.query.count()
    ads_report = fully_ads_report(1, ads_count, None).get_json().get('data')

    # 初始化统计变量
    improved_acos = 0
    worsened_acos = 0
    improved_cvr = 0
    worsened_cvr = 0

    # 遍历 final_result 进行统计
    for item in ads_report.get('final_result', []):
        # 获取 total_list
        total_list = item['ads_list'][2]['total_list']
        acos_difference = float(total_list['acos_difference'].replace('%', ''))
        cvr_difference = float(total_list['cvr_difference'].replace('%', ''))

        # 判断 acos_difference
        if acos_difference <= 0:
            improved_acos += 1  # ACOS 变好
        else:
            worsened_acos += 1  # ACOS 变差

        # 判断 cvr_difference
        if cvr_difference >= 0:
            improved_cvr += 1  # CVR 变好
        else:
            worsened_cvr += 1  # CVR 变差

    print("变好的ACOS数量:", improved_acos)
    print("变坏的ACOS数量:", worsened_acos)
    print("变好的CVR数量:", improved_cvr)
    print("变坏的CVR数量:", worsened_cvr)

    return {
        "users_count": user_count,
        "companies_count": company_count,
        "shop_count": shop_count,
        "ads_count": ads_count,
        "improved_acos": improved_acos,
        "worsened_acos": worsened_acos,
        "improved_cvr": improved_cvr,
        "worsened_cvr": worsened_cvr,
    }