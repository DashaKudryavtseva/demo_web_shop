# <a id="title1">Выпускной проект, в котором описаны API и UI тесты для сайта _DemoWebShop_</a>

[DemoWebShop](https://demowebshop.tricentis.com/) - тестовая платформа, в которой реализован функционал онлайн магазина


## Технологический стек

 ![Python](/src/Python_logo_and_wordmark.png)![Pytest](/src/Pytest_logo.png)![selene](/src/selene.png)![Selenium](/src/Selenium.png)![requests](/src/requests.png)![Allure Report](/src/Allure_Report.png)![Jenkins](/src/Jenkins.png)![Telegram](/src/Telegram.png)

## Покрытый функционал

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

В UI-тестах реализована авторизация через API при помощи фикстуры open_browser_through_api.
Также UI-тесты на добавление товаров в корзину, в wishlist, и в лист сравнения параметризованы по категориям 

## Запуск тестов

### [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/04-little_didi-demowebshop/)

Необходимо выбрать "Собрать с параметрами".

![Jenkins](/src/jenkins_job_main.png)

Далее выбрать тесты для запуска: api или ui. Также можно изменить название для телеграм отчета, например указав, что были запущены API тесты.

![Jenkins](/src/jenkins_job_params.png)

Результат о прохождении тестов присылается в телеграм, со ссылкой на Allure отчет.

![Telegram Notifications](/src/telegram_notofications.png)

### __Примеры Allure отчётов:__ 

#### [Allure Report](https://jenkins.autotests.cloud/job/04-little_didi-demowebshop/allure/)

UI-тесты

 ![Allure UI](/src/allure_ui_tests_1.png)

API-тесты

 ![Allure API](/src/allure_api_tests_2.png)

