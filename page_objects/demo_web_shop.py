from selene import browser, have, command
from utils.url_parts import Endpoints
import random


class DemoWebShop:
    '''Класс описывает методы для работы с UI Demo Web Shop'''

    quantity_to_add: int
    wishlist_quantity: int

    def __init__(self):
        self.banner_closer = browser.element('#bar-notification .close')

        self.shopping_cart = browser.element('#topcartlink')
        self.wishlist = browser.element('.ico-wishlist')
        self.customer_info = browser.element(
            f'.header-links-wrapper a[href="{Endpoints.CUSTOMER}"]'
        )

    def choose_category(self, category_name):
        browser.element(f'.top-menu a[href="{category_name}"]').click()

    def choose_subcategory(self, sub_category):
        browser.element(
            f'.sub-category-item > .title > a[href="{sub_category}"]'
        ).click()

    @property
    def cart_quantity(self):
        empty_cart = browser.element('.order-summary-content').wait_until(
            have.text('Your Shopping Cart is empty!')
        )
        if empty_cart:
            return 0
        else:
            return len(browser.all('.cart-item-row'))

    @property
    def get_products_available_to_add(self):
        browser.element('#newsletter-subscribe-button').perform(
            command.js.scroll_into_view
        )
        products = browser.all('.product-item input[value="Add to cart"]')
        self.quantity_to_add = len(products)
        return products

    @property
    def get_all_products_on_page(self):
        browser.element('.side-2').perform(command.js.scroll_into_view)
        products = browser.all('.product-item>.picture>a')
        return products

    def add_simple_products_to_cart(self):
        for el in self.get_products_available_to_add:
            el.click()
            browser.with_(timeout=3).wait_until(have.text('product has been added'))
            self.banner_closer.click()

    def add_to_wishlist_list(self):
        self.get_products_available_to_add[0].click()
        browser.element('.add-to-cart [id^="add-to-wishlist"]').click()

    def add_to_compare_list(self, num):
        self.get_all_products_on_page[num].click()
        browser.element('.compare-products input').click()

    def add_new_address(self):
        browser.element(f'.list a[href="{Endpoints.CUSTOMER_ADDRESSES}"]').click()
        browser.element('.add-button>[value="Add new"]').click()

    def remove_product_from_cart(self):
        if self.cart_quantity != 0:
            browser.all('.cart-item-row [name="removefromcart"]')[0].click()
            browser.element('.buttons [name="updatecart"]').click()

    def should_quantity_products_in_cart(self):
        self.shopping_cart.perform(command.js.scroll_into_view)
        assert browser.element('.cart-qty').should(
            have.text(f'({self.quantity_to_add})')
        )

    def should_quantity_products_in_wishlist(self, sum):
        self.wishlist.perform(command.js.scroll_into_view)
        assert browser.element('.wishlist-qty').should(have.text(f'({sum})'))

    def should_quantiy_products_in_compare_list(self, num):
        assert browser.all('.product-name .a-center').should(have.size(num))

    def should_remove_success(self, init_qty):
        assert self.cart_quantity < init_qty

    def remove_all_cart(self):
        if self.cart_quantity != 0:
            products = browser.all('.cart-item-row [name="removefromcart"]')
            for p in products:
                p.click()
            browser.element('.buttons [name="updatecart"]').click()
