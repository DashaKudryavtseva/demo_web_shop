from selene import browser, have, command
from utils.url_parts import Endpoints


class DemoWebShop:
    quantity: int
    wishlist_quantity: int

    def __init__(self):
        self.banner_closer = browser.element('#bar-notification .close')

        self.shopping_cart = browser.element('#topcartlink')
        self.wishlist = browser.element('.ico-wishlist')

        self.books = browser.element(f'.top-menu a[href="{Endpoints.BOOKS}"]')
        self.computers = browser.element(f'.top-menu a[href="{Endpoints.COMPUTERS}"]')
        self.desctops = browser.element(f'.item-box a[href="{Endpoints.DESKTOPS}"]')
        self.notebooks = browser.element(f'.top-menu a[href="{Endpoints.NOTEBOOKS}"]')
        self.accessories = browser.element(
            f'.top-menu a[href="{Endpoints.ACCESSORIES}"]'
        )
        self.electronics = browser.element(
            f'.top-menu a[href="{Endpoints.ELECTRONICS}"]'
        )
        self.camera_photo = browser.element(
            f'.top-menu a[href="{Endpoints.CAMERA_PHOTO}"]'
        )
        self.cell_phones = browser.element(
            f'.top-menu a[href="{Endpoints.CELL_PHONES}"]'
        )
        self.apparel_shoes = browser.element(
            f'.top-menu a[href="{Endpoints.APPAREL_SHOES}"]'
        )
        self.digital_downloads = browser.element(
            f'.top-menu a[href="{Endpoints.DIGITAL_DOWNLOADS}"]'
        )
        self.jewelry = browser.element(f'.top-menu a[href="{Endpoints.JEWELRY}"]')
        self.gift_cards = browser.element(f'.top-menu a[href="{Endpoints.GIFT_CARDS}"]')

        self.customer_info = browser.element(
            f'.header-links-wrapper a[href="{Endpoints.CUSTOMER}"]'
        )

    @property
    def get_products_available_to_add(self):
        browser.element('#newsletter-subscribe-button').perform(
            command.js.scroll_into_view
        )
        products = browser.all('.product-item input[value="Add to cart"]')
        self.quantity = len(products)
        return products

    def add_simple_products_to_cart(self):
        for el in self.get_products_available_to_add:
            el.click()
            browser.with_(timeout=3).wait_until(have.text('product has been added'))
            self.banner_closer.click()

    def add_to_wishlist_list(self):
        self.get_products_available_to_add[0].click()
        browser.element('.add-to-cart [id^="add-to-wishlist"]').click()

    def should_quantity_products_in_cart(self):
        self.shopping_cart.perform(command.js.scroll_into_view)
        assert browser.element('.cart-qty').should(have.text(f'({self.quantity})'))

    def should_quantity_products_in_wishlist(self, sum):
        self.wishlist.perform(command.js.scroll_into_view)
        assert browser.element('.wishlist-qty').should(have.text(f'({sum})'))
