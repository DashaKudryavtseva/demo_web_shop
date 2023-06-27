import allure
from allure import step
from tests.ui.page_objects.demowebshop_ui import DemoWebShop

page = DemoWebShop()


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное удаление продукта из корзины')
def test_remove_product_from_cart(open_browser_through_api):
    with step('Открытие корзины'):
        page.shopping_cart.click()
        qty = page.cart_quantity

    with step('Удаление продукта из корзины'):
        page.remove_product_from_cart()

    with step('Проверка успешного удаления продукта'):
        page.should_remove_success(qty)


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное удаление продукта из корзины')
def test_remove_all_cart(open_browser_through_api):
    with step('Открытие корзины'):
        page.shopping_cart.click()

    with step('Удаление продукта из корзины'):
        page.remove_all_cart()

    with step('Проверка успешного удаления продукта'):
        assert page.cart_quantity == 0
