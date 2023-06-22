import allure
from allure import step
from page_objects.demo_web_shop import DemoWebShop

page = DemoWebShop()


@allure.tag('ui')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в корзину')
def test_add_some_products_in_cart(open_browser_through_api):
    with step('Открытие вкладки "Books"'):
        page.books.click()

    with step('Добавление в корзину'):
        page.add_simple_products_to_cart()

    with step('Проверка количества товаров в корзине'):
        page.should_quantity_products_in_cart()


@allure.tag('ui')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов в "Wishlist"')
def test_add_product_to_wishlist(open_browser_through_api):
    with step('Открытие вкладки "Jewelry"'):
        page.apparel_shoes.click()

    with step('Добавление товара в wishlist'):
        page.add_to_wishlist_list()

    with step('Проверка количества товаров в wishliste'):
        page.should_quantity_products_in_wishlist(1)


@allure.tag('ui')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление продуктов к сравнению')
def test_add_products_to_compare_list(open_browser_through_api):
    with step('Открытие вкладки "Books"'):
        page.books.click()

    with step('Добавление продукта к сравнению'):
        page.add_to_compare_list(0)

    with step('Проверка наличия продукта в листе сравнения'):
        page.should_quantiy_products_in_compare_list(1)


def test_add_new_address_to_profile(open_browser_through_api):
    with step('Переход в профиль пользователя'):
        page.customer_info.click()

    with step('Открытие вкладки адресов'):
        page.add_new_address()
