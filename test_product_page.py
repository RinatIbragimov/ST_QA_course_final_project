import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage

# ссылки для тестирования задания с параметризацией
"""@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])"""
def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()

    book_name_on_page = page.find_book_name()
    book_price_on_page = page.find_book_price()

    # добавляем книгу в корзину
    page.add_book_to_cart()

    # получаем код
    page.solve_quiz_and_get_code()
    # проверяем, что название и цена книги верные
    page.compare_book_and_price_in_store_and_message(book_name_on_page, book_price_on_page)

@pytest.mark.xfail(reason="Test fails, because there is a message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()

    # добавляем товар в корзину
    page.add_book_to_cart()

    # получаем код
    page.solve_quiz_and_get_code()
    # проверяем, что нет сообщения об успехе
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()

    # проверяем, что нет сообщения об успехе
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Test fails, because there is a message")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)

    # открываем нужную страницу
    page.open()

    # добавляем товар в корзину
    page.add_book_to_cart()

    # получаем код
    page.solve_quiz_and_get_code()

    # проверяем, что нет сообщения об успехе
    page.should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    # проверка, что пользователь "видит" кнопку логина на странице продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    # проверка, что пользователь может перейти на страницу логина со страницы продукта
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем нужную страницу
    page.open()
    # выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    # проверка, что перешли действительно на страницу логина
    login_page.should_be_login_page()
