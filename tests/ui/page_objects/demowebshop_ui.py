from selene import browser, have, command


class DemoWebShop:
    '''Класс описывает методы для работы с UI Demo Web Shop'''

    quantity_to_add: int


    def __init__(self):
        self.banner_closer = browser.element('#bar-notification .close')

        self.shopping_cart = browser.element('#topcartlink')
        self.wishlist = browser.element('.ico-wishlist')

    def choose_category(self, category_name):
        browser.element(f'.top-menu a[href="{category_name}"]').click()

    def choose_subcategory(self, sub_category):
        browser.element(
            f'.sub-category-item > .title > a[href="{sub_category}"]'
        ).click()

    @property
    def calc_cart_quantity(self) -> int:
        self.shopping_cart.perform(command.js.scroll_into_view)
        qty = browser.element('.cart-qty').locate().text
        return int(qty.replace('(', '').replace(')', ''))

    @property
    def calc_wishlist_quantity(self) -> int:
        self.shopping_cart.perform(command.js.scroll_into_view)
        qty = browser.element('.wishlist-qty').locate().text
        return int(qty.replace('(', '').replace(')', ''))

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
        self.get_all_products_on_page[0].click()
        browser.element('.add-to-cart [id^="add-to-wishlist"]').click()
        self.banner_closer.click()

    def add_to_compare_list(self):
        self.get_all_products_on_page[0].click()
        self.this_compare_product = browser.element('.compare-products input').locate().text
        browser.element('.compare-products input').click()


    def remove_product_from_cart(self):
        if self.calc_cart_quantity != 0:
            browser.all('.cart-item-row [name="removefromcart"]')[0].click()
            browser.element('.buttons [name="updatecart"]').perform(
                command.js.scroll_into_view
            )
            browser.element('.buttons [name="updatecart"]').click()

    def should_addition_products_in_cart(self, qty):
        self.shopping_cart.perform(command.js.scroll_into_view)
        assert self.calc_cart_quantity > qty

    def should_quantity_products_in_wishlist(self, qty):
        self.wishlist.perform(command.js.scroll_into_view)
        assert self.calc_wishlist_quantity > qty

    def should_product_in_compare_list(self):
        assert browser.all('.product-name td a')[0].should(have.text(self.this_compare_product))

    def should_remove_success(self, init_qty):
        assert self.calc_cart_quantity < init_qty

    def remove_all_cart(self):
        if self.calc_cart_quantity != 0:
            products = browser.all('.cart-item-row [name="removefromcart"]')
            for p in products:
                p.click()
            browser.element('.buttons [name="updatecart"]').click()
