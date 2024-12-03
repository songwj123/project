def asin_statistics(asin: str, profile_id: int, region_shop_id: str, start_date=None, end_date=None):
    """
    单个ASIN数据报表，返回 ASIN 的广告数据，并计算每天的总和，同时返回 acos 和 cvr 的字典。
    """
    # 初始化总计数据
    total_list = {
        "kwen_list": {"cvr": 0, "acos": 0},
        "amzn_list": {"cvr": 0, "acos": 0},
        "total_summary": {"total_cvr": 0, "total_acos": 0}
    }
    print("start_date:", start_date, "end_date:", end_date)
    # 初始化日期范围
    if not end_date:
        end_date = datetime.now()
        print(end_date)
    if not start_date:
        start_date = end_date - timedelta(days=30)
        print(start_date)

    # 获取时间列表
    time_range = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in
                  range((end_date - start_date).days + 1)]
    # print(time_range)
    # 初始化每日数据字典
    data_dict = {
        date: {
            "kwen_cost": 0, "kwen_sales": 0, "kwen_purchases_7d": 0, "kwen_clicks": 0,
            "amzn_cost": 0, "amzn_sales": 0, "amzn_purchases_7d": 0, "amzn_clicks": 0
        } for date in time_range
    }
    # print(data_dict)
    # 查询数据库
    # all_data = AdInfoTmp.query.filter(
    #     AdInfoTmp.profile_id == profile_id,
    #     AdInfoTmp.asin == asin,
    #     AdInfoTmp.region_shop_id == region_shop_id,
    #     AdInfoTmp.campaign_date >= start_date,
    #     AdInfoTmp.campaign_date <= end_date
    # ).with_entities(
    #     AdInfoTmp.policy_type,
    #     AdInfoTmp.asin,
    #     AdInfoTmp.ACOS,
    #     AdInfoTmp.CVR,
    #     AdInfoTmp.sales,
    #     AdInfoTmp.purchases_7d,
    #     AdInfoTmp.cost,
    #     AdInfoTmp.clicks,
    #     AdInfoTmp.campaign_date
    # ).distinct().order_by(AdInfoTmp.campaign_date.desc()).all()
    all_data = db.session.query(
        AdInfoTmp.asin,
        AdInfoTmp.policy_type,
        AdInfoTmp.impressions,
        AdInfoTmp.sales,
        AdInfoTmp.cost,
        AdInfoTmp.purchases_7d,
        AdInfoTmp.clicks,
        AdInfoTmp.asin_date,
        AdInfoTmp.campaign_date
    ).filter(
        AdInfoTmp.profile_id == profile_id,
        AdInfoTmp.asin == asin,
        AdInfoTmp.region_shop_id == region_shop_id,
    ).all()
    print(all_data)
    # 累加每天的数据
    for record in all_data:
        date_str = record.campaign_date.strftime('%Y-%m-%d')
        if date_str in data_dict:
            if record.policy_type == '刻纹策略':
                data_dict[date_str]['kwen_cost'] += record.cost
                data_dict[date_str]['kwen_sales'] += record.sales
                data_dict[date_str]['kwen_purchases_7d'] += record.purchases_7d
                data_dict[date_str]['kwen_clicks'] += record.clicks
            else:
                data_dict[date_str]['amzn_cost'] += record.cost
                data_dict[date_str]['amzn_sales'] += record.sales
                data_dict[date_str]['amzn_purchases_7d'] += record.purchases_7d
                data_dict[date_str]['amzn_clicks'] += record.clicks

    # 计算每日 ACOS 和 CVR
    data_list = []
    for date, values in data_dict.items():
        # 刻纹策略 ACOS 和 CVR
        kwen_acos = f"{round(values['kwen_cost'] / values['kwen_sales'] * 100, 2):.2f}" if values[
                                                                                               'kwen_sales'] > 0 else "0.00"
        kwen_cvr = f"{round(values['kwen_purchases_7d'] / values['kwen_clicks'] * 100, 2):.2f}" if values[
                                                                                                       'kwen_clicks'] > 0 else "0.00"
        # 其他策略 ACOS 和 CVR
        amzn_acos = f"{round(values['amzn_cost'] / values['amzn_sales'] * 100, 2):.2f}" if values[
                                                                                               'amzn_sales'] > 0 else "0.00"
        amzn_cvr = f"{round(values['amzn_purchases_7d'] / values['amzn_clicks'] * 100, 2):.2f}" if values[
                                                                                                       'amzn_clicks'] > 0 else "0.00"
        data_list.append({
            "amzn_acos": f"{amzn_acos}%",
            "amzn_cvr": f"{amzn_cvr}%",
            "kwen_acos": f"{kwen_acos}%",
            "kwen_cvr": f"{kwen_cvr}%",
            "time": date
        })

    # 计算总的 ACOS 和 CVR
    kwen_cost = sum(v['kwen_cost'] for v in data_dict.values())
    kwen_sales = sum(v['kwen_sales'] for v in data_dict.values())
    kwen_clicks = sum(v['kwen_clicks'] for v in data_dict.values())
    kwen_purchases_7d = sum(v['kwen_purchases_7d'] for v in data_dict.values())
    amzn_cost = sum(v['amzn_cost'] for v in data_dict.values())
    amzn_sales = sum(v['amzn_sales'] for v in data_dict.values())
    amzn_clicks = sum(v['amzn_clicks'] for v in data_dict.values())
    amzn_purchases_7d = sum(v['amzn_purchases_7d'] for v in data_dict.values())

    total_cost = kwen_cost + amzn_cost
    total_sales = kwen_sales + amzn_sales
    total_clicks = kwen_clicks + amzn_clicks
    total_purchases_7d = kwen_purchases_7d + amzn_purchases_7d
    print(f"total_cost: {total_cost}, total_sales: {total_sales}, total_clicks: {total_clicks}, total_purchases_7d: {total_purchases_7d}")
    if amzn_sales > 0:
        total_list['amzn_list']['acos'] = f"{round(amzn_cost / amzn_sales * 100, 2):.2f}"
    else:
        total_list['amzn_list']['acos'] = "0.00"

    if amzn_clicks > 0:
        total_list['amzn_list']['cvr'] = f"{round(amzn_purchases_7d / amzn_clicks * 100, 2):.2f}"
    else:
        total_list['amzn_list']['cvr'] = "0.00"

    if kwen_sales > 0:
        total_list['kwen_list']['acos'] = f"{round(kwen_cost / kwen_sales * 100, 2):.2f}"
    else:
        total_list['kwen_list']['acos'] = "0.00"

    if kwen_clicks > 0:
        total_list['kwen_list']['cvr'] = f"{round(kwen_purchases_7d / kwen_clicks * 100, 2):.2f}"
    else:
        total_list['kwen_list']['cvr'] = "0.00"

    total_list['total_summary'][
        'total_acos'] = f"{round(total_cost / total_sales * 100, 2):.2f}" if total_sales > 0 else "0.00"
    total_list['total_summary'][
        'total_cvr'] = f"{round(total_purchases_7d / total_clicks * 100, 2):.2f}" if total_clicks > 0 else "0.00"

    return success_response(data={
        "total_list": total_list,
        "ads_data": data_list
    })