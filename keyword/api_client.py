# -*- coding: utf-8 -*-
"""
@Time    : 2023/8/26 11:30
@Author  :
@FileName: api_client.py
@Software: PyCharm
"""

import asyncio
import os
import random
from json import JSONDecodeError
from urllib.parse import quote

from requests import request
from retrying import retry

from loguru import logger
from rsync.celery_task.celery_model.amazon_ad_profiles import AmazonAdProfile
from rsync.celery_task.public.common_function import (
    redis_get_authorization,
    statistics_list,
)
from rsync.celery_task.public.connection_db import session_factory_amazon
from .api_response import ApiResponse
from .base_client import BaseClient
from .exceptions import get_exception_for_code
from .marketplaces import Marketplaces


class ApiClient(BaseClient):
    """
    # 请求公共方法
    """
    
    def __init__(self, company_id, user_info, marketplace, profile_id, **kwargs):
        super(ApiClient, self).__init__()
        self.company_id = company_id
        self.user_info = user_info
        user_info_list = user_info.split(":")
        self.region = user_info_list[0]
        self.region_shop_id = user_info_list[-1]
        self.marketplace = marketplace
        self.profile_id = profile_id
        self.seller_id = kwargs.get("seller_id")
        self.kwargs = kwargs
    
    async def headers(self, types):
        """
        # 请求头
        :return:
        """
        headers_res = {
            "User-Agent": self.user_agent,
            "Amazon-Advertising-API-ClientId": os.environ.get("CLIENT_ID"),
            "Authorization": "Bearer %s" % await self.auth,
            "Content-Type": "application/json",
        }
        if types:
            headers_res.update({"Amazon-Advertising-API-Scope": await self.profile})
        return headers_res
    
    @property
    async def current_user(self):
        return {
            "seller_id": self.seller_id,
            "region_shop_id": self.region_shop_id,
            "profile_id": await self.profile,
            "company_id": self.company_id,
            "country_code": self.marketplace,
        }
    
    @property
    async def profile(self):
        """
        # 请求店铺的配置id
        :return:
        """
        session = session_factory_amazon()
        try:
            profile_info = (
                session.query(AmazonAdProfile.profile_id)
                .filter(
                    AmazonAdProfile.company_id == self.company_id,
                    AmazonAdProfile.region_shop_id == self.region_shop_id,
                    AmazonAdProfile.country_code == self.marketplace,
                    AmazonAdProfile.profile_id == self.profile_id,
                )
                .first()
            )
        finally:
            session.close()
        
        if not profile_info:
            logger.warning(
                f"profileID请求失败-{profile_info}-{self.company_id}-{self.region_shop_id}—{self.marketplace}-{self.profile_id}"
            )
            return None
        
        profile_id = profile_info.profile_id
        self.profile_id = profile_id
        return str(self.profile_id)
    
    @property
    async def auth(self) -> str:
        """
        # 请求返回参数
        :return:
        """
        return await redis_get_authorization(self.user_info)
    
    @retry(stop_max_attempt_number=3, wait_fixed=1000)
    async def _request(
            self,
            data: str = None,
            params: dict = None,
            headers=None,
            timeout=None,
            proxies=None,
            verify=None,
            types=True,
            retry_times=3,
            **kwargs,
    ) -> ApiResponse or None:
        method = kwargs.pop("method", "GET")
        path = kwargs.pop("path", "/")
        
        if params is None:
            params = {}
        
        api_header = await self.headers(types)
        headers_scop = api_header.get("Amazon-Advertising-API-Scope")
        headers_client_id = api_header.get("Amazon-Advertising-API-ClientId")
        headers_authorization = api_header.get("Authorization")
        
        if statistics_list(headers_authorization) < 20:
            logger.warning(f"headers头拼接失败")
            return None
        
        if types:
            if headers_scop is None or headers_client_id is None:
                logger.warning(f"headers头拼接失败")
                return None
        else:
            if headers_client_id is None:
                logger.warning(f"headers头拼接失败")
                return None
        
        if headers is None:
            base_header = api_header.copy()
            base_header.pop("Content-Type")
            headers = base_header
        elif headers is not None:
            base_header = api_header.copy()
            base_header.update(headers)
            headers = base_header
        
        url_path = "{}{}".format(Marketplaces[self.region].endpoint, path)
        
        request_data = data if method in ("POST", "PUT", "PATCH") else None
        
        initial_times = 0
        for retry_times in range(retry_times):
            initial_times += 1
            
            try:
                res = request(
                    method,
                    url_path,
                    params=params,
                    data=request_data,
                    headers=headers or api_header,
                    timeout=timeout,
                    proxies=proxies,
                    verify=verify,
                )
            except Exception as error:
                error_info = {"Message": "request请求失败", "Errors": error.__str__()}
                logger.error(error_info)
                raise Exception(f"{error}")
            
            if os.environ.get("DEBUG", False):
                if params:
                    str_query = "&".join(f"{key}={quote(str(value))}" for key, value in params.items())
                    message = f"{method} {url_path}?{str_query}"
                else:
                    message = method + " " + url_path
                
                logger.info(f"_request次数：{initial_times} - {message}")
            
            api_response, retry_res = await self._check_response(res)
            if api_response and retry_res:
                return api_response
            elif retry_res:
                return None
            else:
                await asyncio.sleep(random.randint(1, 2))
                continue
        return None
    
    async def _check_response(self, res) -> [ApiResponse, bool]:
        headers = vars(res).get("headers")
        status_code = vars(res).get("status_code")
        
        if 200 <= res.status_code < 300:
            try:
                js = res.json() or {}
            except JSONDecodeError:
                js = {}
            
            if isinstance(js, dict):
                next_token = js.get("nextToken", "") or vars(res).get("_next")
                return ApiResponse(js, next_token, headers=headers), True
            else:
                return ApiResponse(js, headers=headers), True
        elif res.status_code == 429:
            # TODO 429 进行重试请求
            logger.warning(f"Amazon：返回429-限速-{self.user_info}")
            return None, False
        else:
            try:
                js = res.json()
            except JSONDecodeError:
                js = res.content
            
            exception = get_exception_for_code(res.status_code)
            if res.status_code == 401:
                # TODO 店铺关到小黑屋-修改redis同步时间 - 401不进行重试
                logger.warning(f"Amazon：返回401-店铺授权失效-{self.user_info}")
                return None, True
            else:
                raise exception(status_code, js, headers)
