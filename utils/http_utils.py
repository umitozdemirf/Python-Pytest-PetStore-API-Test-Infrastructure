import requests

from config.base_config import BaseConfig


class HTTPUtils:

    @staticmethod
    def service_get(url, headers, params=None):
        response = requests.get(url,
                                headers=headers,
                                params=params)
        return response

    @staticmethod
    def service_post(url, body, headers):
        response = requests.post(url,
                                 data=body,
                                 headers=headers)
        return response

    @staticmethod
    def service_put(url, headers, body=None):
        response = requests.put(url,
                                data=body,
                                headers=headers)
        return response

    @staticmethod
    def service_patch(url, body, headers):
        response = requests.patch(url,
                                  data=body,
                                  headers=headers)
        return response

    @staticmethod
    def service_delete(url, headers):
        response = requests.delete(url,
                                   headers=headers)
        return response
