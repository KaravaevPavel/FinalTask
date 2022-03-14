import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector as mysql
from pages.main_page import MainPage
from pages.user_setting_page import UserSettingPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from api.api_service import APIService
from db.sql_service import SQLService


@pytest.fixture(scope='session')
def chromedriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def main_page(chromedriver):
    return MainPage(chromedriver)


@pytest.fixture(scope='session')
def basket_page(chromedriver):
    return BasketPage(chromedriver)


@pytest.fixture(scope='session')
def user_setting_page(chromedriver):
    return UserSettingPage(chromedriver)


@pytest.fixture(scope='session')
def product_page(chromedriver):
    return ProductPage(chromedriver)


@pytest.fixture(scope='session')
def open_site(chromedriver):
    chromedriver.get("http://localhost/litecart/en/")


@pytest.fixture(scope='session')
def sql_connection():
    connection = mysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='litecart')

    yield connection
    connection.close()


@pytest.fixture(scope='session')
def sql_service(sql_connection):
    return SQLService(sql_connection)


@pytest.fixture(scope="session")
def login(main_page):
    main_page.login(f"{os.getenv('email')}", f"{os.getenv('pass_for_litecart')}")


@pytest.fixture(scope="session")
def api_service():
    return APIService()
