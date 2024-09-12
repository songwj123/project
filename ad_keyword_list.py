import asyncio
import traceback

import requests
from flask import request
from venv import logger
from rsync.celery_task.public.api_base import AdvertisingApiException
from srv.app.api_server.ad_server.ad_operation_keyword_server import AdKeywordsApi


def get_common_info():
    """
    获取共享的公司信息
    return
    """
    profile = request.profile
    payload = request.payload
    company_id = payload.get("company_id")
    country = profile.get('country')
    profile_id = profile.get('profile_id')
    region_shop_id = profile.get("region_shop_id")
    region = profile.get("region")

    if None in [company_id, country, profile_id, region_shop_id]:
        return None

    return {
        "company_id": company_id,
        "user_info": f"{region}:advertising:{region_shop_id}",
        "marketplace": country,
        "profile_id": profile_id
    }


def get_keyword_recommendations_v2(asins):
    """
    获取 V2 版本的关键词推荐
    param asins: ASIN 列表
    return: V2 版本的关键词列表
    """

    async def v2_method(api, data):
        params = {"maxNumSuggestions": 1000}
        path = {"asins": data}
        return await api.sp_asin_gets_the_keyword_v2_version(params=params, path=path)

    return asyncio.run(fetch_keywords(v2_method, asins))


def get_keyword_recommendations_v3(asins):
    """
    获取 V3 版本的关键词推荐
    param asins: ASIN 列表
    return: V3 版本的关键词列表
    """

    async def v3_method(api, data):
        body = {
            "recommendationType": "KEYWORDS_FOR_ASINS",
            "asins": data,
            "maxRecommendations": 200,
            "sortDimension": "CLICKS",
            "locale": "en_US",
            "biddingStrategy": "AUTO_FOR_SALES",
            "bidsEnabled": True
        }
        return await api.sp_asin_gets_the_keyword_v3_version(body=body)

    return asyncio.run(fetch_keywords(v3_method, asins))


async def fetch_keywords(api_method, data):
    """
    异步调用 API 并获取关键词
    param api_method: 调用的 API 方法
    param data: 传递给 API 方法的数据
    return
    """
    info = get_common_info()
    if info is None:
        return None

    keywords_api = AdKeywordsApi(**info)

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        api_res = await api_method(keywords_api, data)
        keyword_list = api_res.payload
        return [r['keyword'] for r in keyword_list]
    except AdvertisingApiException:
        logger.error(traceback.format_exc())
        return None
