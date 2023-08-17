from enum import Enum


class Endpoints(str, Enum):
    LOGIN = '/login'
    CUSTOMER = '/customer/info'
    CUSTOMER_ADDRESSES = '/customer/addresses'
    BOOKS = '/books'
    COMPUTERS = '/computers'
    DESKTOPS = '/desktops'
    NOTEBOOKS = '/notebooks'
    ACCESSORIES = '/accessories'
    ELECTRONICS = '/electronics'
    CAMERA_PHOTO = '/camera-photo'
    CELL_PHONES = '/cell-phones'
    APPAREL_SHOES = '/apparel-shoes'
    DIGITAL_DOWNLOADS = '/digital-downloads'
    JEWELRY = '/jewelry'
    GIFT_CARDS = '/gift-cards'

    def __str__(self) -> str:
        return self.value
