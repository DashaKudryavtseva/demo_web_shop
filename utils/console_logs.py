import logging

import curlify as curlify
import allure
from allure import attachment_type


def logs_for_requests(function):
    def wrapper(*args, **kwargs):
        responce = function(*args, **kwargs)
        curl = curlify.to_curl(responce.request)
        curl_log = f'Status code: {responce.status_code} {curl}'


        logging.info(curl)
        allure.attach(curl_log, name='Curl Log', attachment_type=attachment_type.TEXT)
        allure.attach(
            responce.text, name='Response', attachment_type=attachment_type.TEXT
        )
        return responce

    return wrapper
