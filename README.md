# <a id="title1">Выпускной проект, в котором описаны API и UI тесты для сайта _DemoWebShop_</a>

---
[DemoWebShop](https://demowebshop.tricentis.com/) - тестовая платформа, в которой реализован функционал онлайн магазина


## Технологический стек

---
 ![Python](/src/Python_logo_and_wordmark.png)![Pytest](/src/Pytest_logo.png)![selene](/src/selene.png)![Selenium](/src/Selenium.png)![requests](/src/requests.png)![Allure Report](/src/Allure_Report.png)

## Покрытый функционал

---
1. UI
    - Добавление товаров в корзину
    - Добавление товаров в Wishlist
    - Добавление товаров к сравнению
    - Удаление товара из корзины
    - Удаление всех товаров из корзины
2. API
   - Добавление товара без параметров 
   - Дабвление товаров с параметрами
   - Добавление нового адреса в профиль пользователя

## Особенности тестов

---
В UI-тестах реализована авторизация через API при помощи фикстуры open_browser_through_api.
Также UI-тесты на добавление товаров в корзину, в wishlist, и в лист сравнения параметризованы по категориям 

## Примеры отчетов о прохождении тестов

---
### UI-тесты
 ![Allure UI](/src/allure_ui_tests_1.png)
### API-тесты
 ![Allure API](/src/allure_api_tests_2.png)

