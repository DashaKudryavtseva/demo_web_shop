


'''
def test_add_book_in_cart_with_object_model():
    ''Успешное добавление товара в корзину''
    with step('Login through API'):
        demoshop = DemoShop()
        demoshop.login(LOGIN, PASSWORD)

    with step('Add products in cart'):
        cart = demoshop.add_product(13)
        cart = demoshop.add_product(43)

    with step('Assert additional status'):
        assert cart.additional_sucsess_status is True

    with step('Assert quantity of products in cart'):
        assert cart.quantity_of_products == '(4)'
'''