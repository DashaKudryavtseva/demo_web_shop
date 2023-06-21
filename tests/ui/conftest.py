import os

import pytest
from selene import browser
from allure import step

from utils.redefenitions import BaseSession
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='session')
def api_ui_client():
    client = BaseSession(base_url="http://demowebshop.tricentis.com")
    return client


@pytest.fixture(scope='session')
def browser_configuration():
    browser.config.base_url = 'http://demowebshop.tricentis.com'
    yield browser
    with step('Закрыли браузер'):
        browser.quit()


@pytest.fixture(scope='session')
def login_admin_ui(api_ui_client):
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    payload = {'Email': login, 'Password': password}

    api_ui_client.request(
        method='post',
        url='/login',
        params=payload,
        headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
        allow_redirects=False,
    )

    return api_ui_client


@pytest.fixture(scope='session')
def open_browser_through_api(login_admin_ui, browser_configuration):
    # with step("Открываем браузер с предустановленными cookies"):
    token = login_admin_ui.cookies.get('NOPCOMMERCE.AUTH')

    browser.open("")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": token})
    browser.open("")
