# Copyright 2022 Expedia, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import platform
from typing import Union

from furl import furl

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.configuration.client_config import ClientConfig

from .models import (
    Error,
    ExtendedError,
    OrderPurchaseScreenRequest,
    OrderPurchaseScreenResponse,
    OrderPurchaseUpdateRequest,
)


class FraudPreventionClient:
    def __init__(self, client_config: ClientConfig):
        python_version = platform.python_version()
        os_name, os_version = platform.platform().split('-')[:2]
        sdk_metadata = f'open-world-sdk-python-fraudprevention/0.4.0'

        self.__api_client = ApiClient(client_config)
        self.__user_agent = f'{sdk_metadata} (Python {python_version}; {os_name} {os_version})'

    def screen(self, content_type: str = None, body: OrderPurchaseScreenRequest = None) -> Union[OrderPurchaseScreenResponse, ExtendedError, Error]:
        headers = {
            'content-type': content_type,
        }

        query = {}

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/fraud-prevention/order/purchase/screen'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(
            headers=headers, method='post', body=body, response_models=[OrderPurchaseScreenResponse, ExtendedError, Error], url=request_url
        )

    def update(self, content_type: str = None, body: OrderPurchaseUpdateRequest = None) -> Union[None, ExtendedError, Error]:
        headers = {
            'content-type': content_type,
        }

        query = {}

        request_url = furl(self.__api_client.endpoint)
        request_url /= f'/fraud-prevention/order/purchase/update'
        request_url.query.set(query)
        request_url.path.normalize()

        return self.__api_client.call(headers=headers, method='post', body=body, response_models=[None, ExtendedError, Error], url=request_url)