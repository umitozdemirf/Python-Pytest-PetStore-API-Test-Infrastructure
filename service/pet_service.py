import json
import sys

from config.service_config import ServiceConfig
from utils.assertion_utils import Assertion
from utils.http_utils import HTTPUtils
from utils.data_utils import DataUtils
from config.base_config import BaseConfig


class PetService:

    @staticmethod
    def get_pets_by_status(status):
        path = ServiceConfig.PET + ServiceConfig.FIND_BY_STATUS
        url = BaseConfig.API_URL + path

        params = {'status': status}
        headers = {'Content-Type': "application/json"}

        response = HTTPUtils.service_get(url,
                                         headers,
                                         params)

        Assertion.status_check(response, 200)
        Assertion.null_check("Response", response.json())

        sys.stdout.write(f'\nGot pets with status from service\n')
        return response.json()

    @staticmethod
    def create_pet(pet_body):
        url = BaseConfig.API_URL + ServiceConfig.PET

        headers = {'Content-Type': "application/json"}

        response = HTTPUtils.service_post(url,
                                          json.dumps(pet_body),
                                          headers)
        Assertion.status_check(response, 200)  # The resp code should normally be 201, but they are using 200!
        Assertion.null_check("Response", response.json())

        sys.stdout.write(f'\nCreated pet from service\n')
        return response.json()

    @staticmethod
    def update_pet(pet_body):
        url = BaseConfig.API_URL + ServiceConfig.PET

        headers = {'Content-Type': "application/json"}

        response = HTTPUtils.service_put(url, headers, json.dumps(pet_body))

        Assertion.status_check(response, 200)  # The resp code should normally be 203, but they are using 200!

        sys.stdout.write(f'\nUpdated pet with body from service\n')
        return response.json()

    @staticmethod
    def delete_pet(pet_id):
        path = f'{ServiceConfig.PET}/{pet_id}'
        url = BaseConfig.API_URL + path

        headers = {'Content-Type': "application/json"}

        response = HTTPUtils.service_delete(url, headers)

        Assertion.status_check(response, 200)  # The resp code should normally be 202 or 204, but they are using 200!

        sys.stdout.write(f'\nDeleted pet with ID: {pet_id} from service\n')
        return response.json()
