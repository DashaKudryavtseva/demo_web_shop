from selene import browser, have
from allure import step


from page_objects.demo_web_shop import DemoWebShop


def test_add_some_products_in_cart(open_browser_through_api):
    page = DemoWebShop()

    with step('Открытие вкладки "Books"'):
        page.books.click()

    with step('Добавление в корзину'):
        page.add_simple_products_to_cart()

    with step('Проверка количества товаров в корзине'):
        page.should_quantity_products_in_cart()


def test_add_product_to_wishlist(open_browser_through_api):
    page = DemoWebShop()

    with step('Открытие вкладки "Jewelry"'):
        page.apparel_shoes.click()

    with step('Добавление товара в wishlist'):
        page.add_to_wishlist_list()

    with step('Проверка количества товаров в wishliste'):
        page.should_quantity_products_in_wishlist(1)
