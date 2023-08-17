import allure
import pytest
from tests.ui.page_objects.demowebshop_ui import DemoWebShop
from demo_web_shop.utils.url_parts import Endpoints

page = DemoWebShop()


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в корзину')
@pytest.mark.parametrize(
    'category',
    [Endpoints.BOOKS, Endpoints.DIGITAL_DOWNLOADS],
    ids=["Books", "Digital Downloads"],
)
def test_add_some_products_in_cart(open_browser_through_api, category):
    init_qty = page.calc_cart_quantity

    page.choose_category(category)
    page.add_simple_products_to_cart()
    page.should_addition_products_in_cart(init_qty)


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в "Wishlist"')
@pytest.mark.parametrize(
    'category',
    [Endpoints.APPAREL_SHOES, Endpoints.DIGITAL_DOWNLOADS],
    ids=["Apparel&Shoes", "Digital Downloads"],
)
def test_add_product_to_wishlist(open_browser_through_api, category):
    init_qty = page.calc_wishlist_quantity

    page.choose_category(category)
    page.add_to_wishlist_list()
    page.should_quantity_products_in_wishlist(init_qty)


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов к сравнению')
@pytest.mark.parametrize(
    'category',
    [
        Endpoints.BOOKS,
        Endpoints.DIGITAL_DOWNLOADS,
        Endpoints.APPAREL_SHOES,
        Endpoints.GIFT_CARDS,
    ],
    ids=["Books", "Digital Downloads", "Apparel&Shoes", "Gift Cards"],
)
def test_add_product_to_compare_list(open_browser_through_api, category):
    page.choose_category(category)
    page.add_to_compare_list()
    page.should_product_in_compare_list()
