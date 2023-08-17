import os

from demo_web_shop.data.user_info import UserAddress
from tests.api.models.cart import Cart

from dotenv import load_dotenv

from demo_web_shop.utils.redefenitions import BaseSession

load_dotenv()


class DemoShop:
    quantity_of_products: str

    def __init__(self):
        self.demoshop_session = BaseSession(base_url=os.getenv('base_url'))
        self.__url_for_simple_addition = '/addproducttocart/catalog'
        self.__url_for_addition_with_details = '/addproducttocart/details'
        self.__url_for_address_addition = '/customer/addressadd'
        self.cart: Cart
        self.__cart_url = '/cart'

    def login(self, email, password):
        auth_cookie_name = 'NOPCOMMERCE.AUTH'
        responce = self.demoshop_session.post(
            url='/login',
            params={'Email': email, 'Password': password},
            headers={
                'content-type': "application/x-www-form-urlencoded; charset=UTF-8"
            },
            allow_redirects=False,
        )
        auth_cookie = responce.cookies.get(auth_cookie_name)
        self.demoshop_session.cookies.set(auth_cookie_name, auth_cookie)
        return self

    def add_simple_product(self, id_product):
        responce = self.demoshop_session.post(
            url=f'{self.__url_for_simple_addition}/{id_product}/1/1'
        ).json()
        self.cart = Cart(json=responce)

    def add_product_with_params(self, id_product):
        data = {
            f'product_attribute_{id_product}_5_18': 53,
            f'product_attribute_{id_product}_6_19': 54,
            f'product_attribute_{id_product}_3_20': 57,
            f'addtocart_{id_product}.EnteredQuantity': 1,
        }
        responce = self.demoshop_session.post(
            url=f'{self.__url_for_addition_with_details}/{id_product}/1', data=data
        ).json()
        print(responce)
        self.cart = Cart(json=responce)

    def add_new_address_to_user_profile(self, user_address: UserAddress):
        data = {
            'Address.Id': 0,
            'Address.FirstName': user_address.first_name,
            'Address.LastName': user_address.last_name,
            'Address.Email': user_address.email,
            'Address.Company': user_address.company,
            'Address.CountryId': user_address.country_id,
            'Address.StateProvinceId': user_address.state_id,
            'Address.City': user_address.city,
            'Address.Address1': user_address.address1,
            'Address.Address2': user_address.address2,
            'Address.ZipPostalCode': user_address.zip_or_postal_code,
            'Address.PhoneNumber': user_address.phone_number,
            'Address.FaxNumber': user_address.fax_number,
        }
        responce = self.demoshop_session.post(
            url=f'{self.__url_for_address_addition}', data=data
        )
        return responce.status_code
