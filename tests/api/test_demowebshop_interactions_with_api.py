import os
import allure
from dotenv import load_dotenv
from allure import step

from data.user_info import UserAddress

load_dotenv()

LOGIN = os.getenv('user_login')
PASSWORD = os.getenv('user_password')

address_info = UserAddress(
    'Ivan',
    'Ivanov',
    'iivanov@gmail.com',
    'Male',
    'Google',
    'Russia',
    66,
    '',
    0,
    'Kazan',
    'Sport Street, 10',
    '',
    '123456',
    '89876543210',
    '',
)


@allure.tag('API')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление товара из раздела "BOOKS" в корзину')
def test_add_book_in_cart(dws_session):
    with step('Добавление товара в корзину'):
        dws_session.add_simple_product(43)

    with step('Проверка статуса добавления'):
        assert dws_session.cart.additional_product_sucsess_status is True


@allure.tag('API')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление товара из раздела "DESKTOPS" в корзину')
def test_add_desktop_in_cart(dws_session):
    with step('Добавление продуктов в корзину'):
        dws_session.add_product_with_params(72)

    with step('Проверка статуса добавления'):
        assert dws_session.cart.additional_product_sucsess_status is True


@allure.tag('API')
@allure.label('owner', 'Daria Kudriavtseva')
@allure.title('Успешное добавление нового адреса в профиль пользователя')
def test_add_address_to_user_profile(dws_session):
    with step('Добавление нового адреса'):
        addition_address_status = dws_session.add_new_address_to_user_profile(
            address_info
        )
    with step('Проверка статуса добавления адреса'):
        assert addition_address_status == 200
