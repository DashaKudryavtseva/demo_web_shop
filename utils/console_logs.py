import logging

import curlify as curlify
import allure
from allure import attachment_type


def logs_for_requests(function):
    def wrapper(*args, **kwargs):
        responce = function(*args, **kwargs)
        content_type = responce.headers.get('content-type')
        curl = curlify.to_curl(responce.request)
        curl_log = f'Status code: {responce.status_code} {curl}'

        if content_type is None:
            logging.info('There is no content on the sent request.')
        elif 'text' in content_type:
            logging.info(f'Content: \n{responce.text}')
        elif 'json' in content_type:
            logging.info(f'Content: \n{responce.json()}')

        logging.info(curl)
        allure.attach(curl_log, name='Curl Log', attachment_type=attachment_type.TEXT)
        allure.attach(
            responce.text, name='Response', attachment_type=attachment_type.TEXT
        )
        return responce

    return wrapper
