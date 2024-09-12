from rsync.celery_task.public.api_base import AdvertisingApiException
from srv.app.api_server.ad_server.ad_operation_keyword_server import AdKeywordsApi
import asyncio
import traceback
from venv import logger
import logging
logger = logging.getLogger(__name__)


class KeywordRecommendationService:
    def __init__(self, company_id, country, profile_id, region_shop_id, region):
        self.company_id = company_id
        self.country = country
        self.profile_id = profile_id
        self.region_shop_id = region_shop_id
        self.region = region
        self.keywords_api = AdKeywordsApi(
            company_id=company_id,
            user_info=f"{region}:advertising:{region_shop_id}",
            marketplace=country,
            profile_id=profile_id
        )

    async def get_keywords_v3(self, asins):
        data = {
            "recommendationType": "KEYWORDS_FOR_ASINS",
            "asins": asins,
            "maxRecommendations": 200,
            "sortDimension": "CLICKS",
            "locale": "en_US",
            "biddingStrategy": "AUTO_FOR_SALES",
            "bidsEnabled": True
        }
        try:
            api_res = await self.keywords_api.sp_asin_gets_the_keyword_v3_version(body=data)
            return [r['keyword'] for r in api_res.payload]
        except AdvertisingApiException:
            logger.error(traceback.format_exc())
            return None

    def get_keywords_v2(self, asins):
        params = {"maxNumSuggestions": 1000}
        path = {"asins": asins}
        try:
            api_res = self.keywords_api.sp_asin_gets_the_keyword_v2_version(params=params, path=path)
            return api_res
        except AdvertisingApiException:
            logger.error(traceback.format_exc())
            return None

    def get_keywords(self, asins):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        v3_keywords = loop.run_until_complete(self.get_keywords_v3(asins))
        v2_keywords = self.get_keywords_v2(asins)
        return {"v2": v2_keywords, "v3": v3_keywords}
