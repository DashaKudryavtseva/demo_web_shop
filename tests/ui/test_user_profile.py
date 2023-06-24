import allure
from allure import step
from tests.ui.page_objects.demo_web_shop import DemoWebShop

page = DemoWebShop()


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в корзину')
def test_add_new_address_to_profile(open_browser_through_api):
    with step('Переход в профиль пользователя'):
        page.customer_info.click()

    with step('Открытие вкладки адресов'):
        page.add_new_address()
