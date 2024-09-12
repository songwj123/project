@task_api.route("/GetKeywordRecommendations-v3", methods=["POST"])
@check_required_params(
    {
        "payload": ["company_id"],
        "profile": ["profile_id"],
        'json': ['asins', 'recommendationType',
                 'maxRecommendations', 'sortDimension', 'locale', 'biddingStrategy', 'bidsEnabled']
    }
)
def get_keyword_recommendations_v3():
    """
    获取V3版本关键词推荐
    :return:
    """
    try:
        request_data = request.json
    except BadRequest:
        return ajax_response.success(message="请求参数有误")

    profile = request.profile
    payload = request.payload
    company_id = payload.get("company_id")
    country = profile.get('country')
    profile_id = profile.get('profile_id')
    region_shop_id = profile.get("region_shop_id")
    region = profile.get("region")
    recommendationtype = request_data.get("recommendationType")
    asins = request_data.get("asins")
    maxrecommendations = request_data.get("maxRecommendations")
    sortdimension = request_data.get("sortDimension")
    locale = request_data.get("locale")
    biddingstrategy = request_data.get("biddingStrategy")
    bidsenabled = request_data.get("bidsEnabled")
    if company_id is None or country is None or profile_id is None or region_shop_id is None:
        return None

    data = {
        "recommendationType": recommendationtype,
        "asins": asins,
        "maxRecommendations": maxrecommendations,
        "sortDimension": sortdimension,
        "locale": locale,
        "biddingStrategy": biddingstrategy,
        "bidsEnabled": bidsenabled
    }

    info = {
            "company_id": company_id,
            "user_info": f"{region}:advertising:{region_shop_id}",
            "marketplace": country,
            "profile_id": profile_id
        }
    print(f"info: {info}")
    keywords_api = AdKeywordsApi(**info)
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        api_res = asyncio.run(keywords_api.sp_asin_gets_the_keyword_v3_version(body=data))
        keyword_list = api_res.payload
        res_list = []
        for r in keyword_list:
            res_list.append(r['keyword'])
        # print(res_list)
        # print(f"api_res: {api_res}")
        return jsonify(res_list)
    except AdvertisingApiException:
        logger.error(traceback.format_exc())
        return jsonify({"message": "操作失败"}, 500)