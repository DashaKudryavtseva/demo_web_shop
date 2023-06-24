import os

from tests.api.models.cart import Cart

from dotenv import load_dotenv

from utils.redefenitions import BaseSession

load_dotenv()


class DemoShop:
    quantity_of_products: str

    def __init__(self):
        self.demoqa = BaseSession(base_url=os.getenv('base_url'))
        self.__url_for_addition = '/addproducttocart/catalog'
        self.cart: Cart

    def login(self, email, password):
        auth_cookie_name = 'NOPCOMMERCE.AUTH'
        responce = self.demoqa.post(
            url='/login',
            params={'Email': email, 'Password': password},
            headers={
                'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
            },
            allow_redirects=False,
        )
        auth_cookie = responce.cookies.get(auth_cookie_name)
        self.demoqa.cookies.set(auth_cookie_name, auth_cookie)
        return self

    def add_product(self, id_product):
        responce = self.demoqa.post(
            url=f'{self.__url_for_addition}/{id_product}/1/1'
        ).json()
        self.cart = Cart(json=responce)
        return self.cart

    @property
    def additional_sucsess_status(self):
        return self.cart.json()['success']
