from rsync.celery_task.ad_request.ad_sb_request.sb_campaigns_list import RequestSbCampaigns

import asyncio

prod_info = {
    "company_id": 1818586553803341824,
    "user_info": "NA:advertising:901723440409076962",
    "marketplace": "US",
    "profile_id": 3854189483301387
}


async def main():
    await RequestSbCampaigns(prod_info).request_sb_campaigns_list()


asyncio.run(main())
