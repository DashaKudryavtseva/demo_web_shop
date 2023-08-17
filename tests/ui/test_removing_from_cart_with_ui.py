import allure
from tests.ui.page_objects.demowebshop_ui import DemoWebShop

page = DemoWebShop()


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное удаление продукта из корзины')
def test_remove_product_from_cart(open_browser_through_api):
    init_qty = page.calc_cart_quantity

    page.remove_product_from_cart()
    page.should_remove_success(init_qty)


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное удаление продукта из корзины')
def test_remove_all_cart(open_browser_through_api):
    page.remove_all_cart()
    page.should_cart_is_empty()
