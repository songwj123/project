# @ad_endpoint("/sp/targets/products/recommendations", method="POST")
# async def sp_asin_get_asins(
#         self, version: int = 3, **kwargs
# ):
#     """
#     获取亚马逊ASIN对应的推荐ASIN
#     """
#     schema_version = "application/vnd.spproductrecommendation.v{}+json".format(
#         version
#     )
#     headers = {
#         "Accept": schema_version,
#         "Content-Type": schema_version,
#     }
#     response = await self._request(
#         data=Utils.convert_body(kwargs.pop("body", None), False),
#         params=kwargs.pop("args", None),
#         headers=headers,
#         **kwargs,
#     )
#     return response

data ={"company_id": "3854189483301387","user_info": f"'NA:advertising:901723440409076962'","marketplace": "US","profile_id": "3854189483301387"}







# def _fetch_get_asins(self, asins: str):
#     """
#          从/GetAsins接口获取关键词对应的asin
#     """
#     asins_list = [asins] if isinstance(asins, str) else list(asins)
#     data = {
#         "adAsins": asins_list,
#         "count": 47,
#         "locale": "en_US"
#     }
#     user_profile_info = self.build_user_profile_info()
#     keywords_api = AdKeywordsApi(**user_profile_info)
#     try:
#         api_res = asyncio.run(keywords_api.sp_asin_get_asins(body=data))
#         return [item['recommendedAsin'] for item in api_res.payload.get('recommendations', [])]
#     except AdvertisingApiException as e:
#         logger.info('invoke _fetch_get_asins : {}'.format(e.get_error()))
#         raise e


# import asyncio
# import json
# from loguru import logger
# from rsync.celery_task.public.api_base import AdvertisingApiException
# from srv.app.api_server.ad_server.ad_operation_keyword_server import AdKeywordsApi
#
#
# def _fetch_get_asins(asins: str):
#     """
#          从/GetAsins接口获取关键词对应的asin
#     """
#     asins_list = [asins] if isinstance(asins, str) else list(asins)
#     data = {
#         "adAsins": asins_list,
#         "count": 47,
#         "locale": "en_US"
#     }
#     dd = {"company_id": "1818586553803341824", "user_info": "NA:advertising:901723440409076962", "marketplace": "US",
#           "profile_id": "3854189483301387"}
#     user_profile_info = dd
#     keywords_api = AdKeywordsApi(**user_profile_info)
#     try:
#         data = json.dumps(data)
#         api_res = asyncio.run(keywords_api.sp_asin_get_asins(body=data))
#         print(api_res.payload)
#         return [item['recommendedAsin'] for item in api_res.payload.get('recommendations', [])]
#     except AdvertisingApiException as e:
#         logger.info('invoke _fetch_get_asins : {}'.format(e.get_error()))
#         raise e
#
#
# print(_fetch_get_asins('B0CZP2ZJV2'))