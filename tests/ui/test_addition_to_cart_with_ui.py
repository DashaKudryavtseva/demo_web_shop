import allure
from allure import step
from tests.ui.page_objects.demowebshop_ui import DemoWebShop
from utils.url_parts import Endpoints

page = DemoWebShop()


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в корзину')
def test_add_some_products_in_cart(open_browser_through_api):
    with step('Открытие вкладки "Books"'):
        page.choose_category(Endpoints.BOOKS)

    with step('Добавление в корзину'):
        page.add_simple_products_to_cart()

    with step('Проверка количества товаров в корзине'):
        page.should_quantity_products_in_cart()


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в "Wishlist"')
def test_add_product_to_wishlist(open_browser_through_api):
    with step('Открытие вкладки "Apparel & Shoes"'):
        page.choose_category(Endpoints.APPAREL_SHOES)

    with step('Добавление товара в wishlist'):
        page.add_to_wishlist_list()

    with step('Проверка количества товаров в wishliste'):
        page.should_quantity_products_in_wishlist(1)


@allure.tag('UI')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов к сравнению')
def test_add_products_to_compare_list(open_browser_through_api):
    with step('Открытие вкладки "Books"'):
        page.choose_category(Endpoints.BOOKS)

    with step('Добавление продукта к сравнению'):
        page.add_to_compare_list(0)

    with step('Проверка наличия продукта в листе сравнения'):
        page.should_quantiy_products_in_compare_list(1)
