# @task_api.route("/GetKeywordList", methods=["POST"])
# def get_keyword_list():
#     """
#     获取关键词列表(大词组，高低词组，否词组)
#     :return
#     """
#     try:
#         request_data = request.json
#     except BadRequest:
#         return jsonify({"message": "请求参数有误"}), 400
#
#     asins = request_data.get("asins")
#     description = request_data.get("description")
#
#     if not asins:
#         return jsonify({"message": "缺少 'asins' 参数"}), 400
#
#     keyword2 = get_keyword_recommendations_v2(asins)
#     keyword3 = get_keyword_recommendations_v3(asins)
#
#     if keyword2 is None or keyword3 is None:
#         return jsonify({"message": "操作失败"}), 500
#
#     data = {
#         "asins": asins,
#         "description": description,
#         "keywords": {
#             "v2": keyword2,
#             "v3": keyword3
#         }
#     }
#
#     url = "http://120.27.208.224:8003/keywords_retrival"
#     try:
#         response = requests.post(url, json=data)
#         return jsonify(response.json())
#     except requests.RequestException:
#         logger.error(traceback.format_exc())
#         return jsonify({"message": "请求外部服务失败"}), 500

@task_api.route("/GetKeywordList", methods=["POST"])
@check_required_params(
    {
        "payload": ["company_id"],
        "profile": ["profile_id"],
        'json': ['asins']
    }
)
def get_keyword_list():
    """
    获取关键词推荐
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
        return ajax_response.success(message="请求参数有误")

    service = KeywordRecommendationService(
        company_id=company_id,
        country=country,
        profile_id=profile_id,
        region_shop_id=region_shop_id,
        region=region
    )

    keyword_data = service.get_keywords(asins)

    description = request_data.get("description")
    data = {
        "asins": asins,
        "description": description,
        "keywords": keyword_data
    }

    url = "http://120.27.208.224:8003/keywords_retrival"
    response = requests.post(url, json=data)
    return response.json()


@task_api.route("/GetKeywordRecommendations-v2", methods=["GET"])
@check_required_params(
    {
        "payload": ["company_id"],
        "profile": ["profile_id"],
        'get': ['asinValue']
    }
)
def get_keyword_recommendations_v2():
    """
    获取V2版本关键词推荐
    :return:
    """
    asinValue = request.args.get("asinValue")
    print(asinValue)
    profile = request.profile
    payload = request.payload
    company_id = payload.get("company_id")
    country = profile.get('country')
    profile_id = profile.get('profile_id')
    region_shop_id = profile.get("region_shop_id")
    region = profile.get("region")
    if company_id is None or country is None or profile_id is None or region_shop_id is None:
        return None

    parms = {
        "maxNumSuggestions": 1000
    }

    path = {
        "asinValue": asinValue,
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
        api_res = asyncio.run(
            keywords_api.sp_asin_gets_the_keyword_v2_version(args=parms, asinValue=path.get("asinValue")))
        print(f"api_res: {api_res}")
        return jsonify(api_res)
    except AdvertisingApiException:
        logger.error(traceback.format_exc())
        return jsonify({"message": "操作失败"}, 500)