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

# data ={"company_id": "3854189483301387","user_info": f"'NA:advertising:901723440409076962'","marketplace": "US","profile_id": "3854189483301387"}



'''
songwj
'''



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
import json
dd = ['car phone mount', 'magsafe car mount', 'car mount', 'cell phone car mount', 'phone mount', 'cell phone holder car', 'phone holder', 'phone holder car', 'car phone holder charger', 'car phone holder mount', 'cell phone holder', 'car vent phone mount', 'suction cup phone mount', 'magnetic phone holder car', 'dashboard cell phone holder', 'wireless car charger mount', 'car phone mount charger', 'iphone holder car', 'car mount iphone', 'dashboard phone holder', 'windshield phone mount', 'suction phone holder', 'suction phone mount', 'cellphone holder car', 'iphone 15 car mount', 'car', 'phone holders your car', 'suction cup phone holder', 'phone stand car', 'truck phone holder', 'pink car phone holder', 'car phone holder vent', 'soporte de telefono para carro', 'car phone holder wireless charger', 'iphone mount', 'cupholder phone holder car', 'car accessories', 'iphone 14 car mount', 'cup phone holder car', 'suction cup mount', 'porta telefono para carro', 'dashboard car phone holder', 'windshield phone mount car', 'rhinestone car phone holder mount', 'porta celular para carro', 'phone holder car windshield', 'pink car phone mount', 'dash phone holder car', 'car mobile holder', 'car phone holders iphone', 'auto phone holder', 'phone mount truck', 'sticky phone mount', 'universal car dashboard phone holder', 'gps holder', 'soporte para celular', 'car phone holder top rated', 'truckers phone mount', 'car tripod', 'universal car phone holders', 'phone car mount dashboard', 'cars stuff', 'sujetador de celular para carro', 'car phone holder mount windshield', 'soporte de celular para carro', 'cell phone accessories', 'one touch car phone holder', 'batman popsocket', 'cell phone holder car windshield', 'mobile phone car holder', 'car electronic', 'electronic mount', 'suction cup cell phone holder', 'phone holder with suction cup', 'car phone holder clip mount', 'car phone mount bundle', 'telephone holder car', 'window phone mount car', 'car phone holder ball mount', 'best phone mount car', 'car phone holder glass mount', 'suction cup car phone mount', 'car phone holder strong suction', 'cupholder car phone mount', 'windshield mounting phone holder', 'nissan rogue 2017', 'phone holder car mirror', 'portacelular para carro', 'soft phone stand', 'best phone holder car', 'car holder mount', 'bmw car phone holder']
print(json.dumps(dd))