import allure
import pytest
from allure import step
from tests.ui.page_objects.demowebshop_ui import DemoWebShop
from utils.url_parts import Endpoints

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

    with step('Открытие вкладки с товарами'):
        page.choose_category(category)

    with step('Добавление в корзину'):
        page.add_simple_products_to_cart()

    with step('Проверка изменения количества товаров в корзине'):
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

    with step('Открытие вкладки с товарами"'):
        page.choose_category(category)

    with step('Добавление товара в wishlist'):
        page.add_to_wishlist_list()

    with step('Проверка изменения количества товаров в "Wishlist"'):
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
    with step('Открытие вкладки с товарами'):
        page.choose_category(category)

    with step('Добавление продукта к сравнению'):
        page.add_to_compare_list()

    with step('Проверка наличия продукта в листе сравнения'):
        page.should_product_in_compare_list()
