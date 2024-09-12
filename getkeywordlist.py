@task_api.route("/GetKeywordList", methods=["POST"])
@check_required_params(
    {
        "payload": ["company_id"],
        "profile": ["profile_id"],
        'json': ['asins']
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
    asins = request_data.get("asins")
    if company_id is None or country is None or profile_id is None or region_shop_id is None:
        return None

    data = {
        "recommendationType": "KEYWORDS_FOR_ASINS",
        "asins": asins,
        "maxRecommendations": 200,
        "sortDimension": "CLICKS",
        "locale": "en_US",
        "biddingStrategy": "AUTO_FOR_SALES",
        "bidsEnabled": True
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


def get_keyword_recommendations_v2():
    """
    获取V2版本关键词推荐
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
    asins = request_data.get("asins")
    if company_id is None or country is None or profile_id is None or region_shop_id is None:
        return None

    params = {
        "maxNumSuggestions": 1000,
    }

    path = {
        "asins": asins,
    }

    info = {
        "company_id": company_id,
        "user_info": f"{region}:advertising:{region_shop_id}",
        "marketplace": country,
        "profile_id": profile_id
    }

    keywords_api = AdKeywordsApi(**info)
    try:
        api_res = keywords_api.sp_asin_gets_the_keyword_v2_version(params=params, path=path)
        return asyncio.run(api_res)
    except AdvertisingApiException:
        logger.error(traceback.format_exc())
        return ajax_response.fail(message="操作失败")


def get_keyword_list():
    try:
        request_data = request.json
    except BadRequest:
        return ajax_response.success(message="请求参数有误")

    asins = request_data.get("asins")
    description = request_data.get("description")
    keyword2 = get_keyword_recommendations_v2(asins=asins)
    keyword3 = get_keyword_recommendations_v3(asins=asins)

    data = {
        "asins": asins,
        "description": description,
        "keywords": {
            "v2": keyword2,
            "v3": keyword3
        }
    }
    url = "http://120.27.208.224:8003/keywords_retrival"
    response = requests.post(url, json=data)
    return response.json()