from requests import Session
from allure import step

from utils import console_logs



class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    @console_logs.logs_for_requests
    def request(self, method, url, **kwargs):
        with step(f'{method} in {url}'):
            responce = super().request(method, url=f'{self.base_url}{url}', **kwargs)
        return responce
