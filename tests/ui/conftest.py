import os

import pytest

from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demo_web_shop.utils import attach
from demo_web_shop.utils.redefenitions import BaseSession
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture()
def api_ui_client():
    client = BaseSession(base_url=os.getenv('base_url'))
    return client


@pytest.fixture()
def browser_configuration():
    options = Options()

    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": '100.0',
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }

    options.capabilities.update(selenoid_capabilities)

    s_login = os.getenv('LOGIN')
    s_password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{s_login}:{s_password}@selenoid.autotests.cloud/wd/hub",
        options=options,
    )
    driver.implicitly_wait(60)
    browser.config.driver = driver

    browser.config.browser_name = "chrome"
    browser.config.base_url = os.getenv('base_url')

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture()
def login_demoshop(api_ui_client):
    login = os.getenv('user_login')
    password = os.getenv('user_password')

    payload = {'Email': login, 'Password': password}

    api_ui_client.request(
        method='post',
        url='/login',
        params=payload,
        headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
        allow_redirects=False,
        verify=False,
    )

    return api_ui_client


@pytest.fixture()
def open_browser_through_api(login_demoshop, browser_configuration):
    token = login_demoshop.cookies.get('NOPCOMMERCE.AUTH')

    browser.open("")
    if browser.element('#main-message').wait_until(
        have.text('Your connection is not private')
    ):
        browser.element('#details-button').click()
        browser.element('#final-paragraph').click()

    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": token})
    browser.open("")
