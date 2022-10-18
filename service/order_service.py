import json
import sys

from config.service_config import ServiceConfig
from utils.assertion_utils import Assertion
from utils.http_utils import HTTPUtils
from utils.data_utils import DataUtils
from config.base_config import BaseConfig


class OrderService:

    @staticmethod
    def create_order(order_body):
        url = BaseConfig.API_URL + ServiceConfig.ORDER

        headers = {'Content-Type': "application/json"}

        response = HTTPUtils.service_post(url, json.dumps(order_body), headers)

        Assertion.status_check(response, 200)  # The resp code should normally be 201, but they are using 200!
        Assertion.null_check("Response", response.json())

        sys.stdout.write(f'\nCreated order from service\n')
        return response.json()
