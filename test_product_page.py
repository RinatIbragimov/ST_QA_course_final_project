import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

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

@pytest.mark.auth_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.LOGIN_PAGE_LINK  # ссылка на страницу логина\регистрации
        self.browser = browser
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = LoginPage(browser, link)
        # открываем нужную страницу
        page.open()

        # генерим тестовую почту, задаем пароль
        email, password = page.make_email_and_password()

        # регистрируем нового пользователя
        page.register_new_user(email, password)

        # проверяем, что пользователь авторизован
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_LINK

        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        # открываем нужную страницу
        page.open()
        # проверяем, что нет сообщения об успехе
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLocators.PRODUCT_PAGE_PROMO

        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        # открываем нужную страницу
        page.open()
        # ищем название и цену книги на странице
        book_name_on_page = page.find_book_name()
        book_price_on_page = page.find_book_price()

        # добавляем книгу в корзину
        page.add_book_to_cart()
        # получаем код
        page.solve_quiz_and_get_code()
        # проверяем, что название и цена книги верные
        page.compare_book_and_price_in_store_and_message(book_name_on_page, book_price_on_page)

def test_guest_cant_see_success_message(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем нужную страницу
    page.open()
    # проверяем, что нет сообщения об успехе
    page.should_not_be_success_message()

def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_PAGE_PROMO

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем нужную страницу
    page.open()
    # ищем название и цену книги на странице
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
    link = ProductPageLocators.PRODUCT_PAGE_LINK
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    # проверка, что пользователь может перейти на страницу логина со страницы продукта
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем нужную страницу
    page.open()
    # выполняем метод страницы: переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    # проверка, что перешли действительно на страницу логина
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLocators.PRODUCT_PAGE_LINK

    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем нужную страницу
    page.open()
    page.go_to_basket_page()
    cart_page = BasketPage(browser, browser.current_url)
    # проверка, что корзина пуста
    cart_page.should_be_cart_is_empty()
