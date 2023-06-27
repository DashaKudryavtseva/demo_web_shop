import os
import pytest
from dotenv import load_dotenv
from allure import step


from tests.api.models.demowebshop_api import DemoShop


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session')
def dws_session():
    demoshop = DemoShop()
    LOGIN = os.getenv('user_login')
    PASSWORD = os.getenv('user_password')

    with step('Вход через API'):
        demoshop.login(LOGIN, PASSWORD)

    return demoshop
