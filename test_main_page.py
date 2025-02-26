import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators, LoginPageLocators
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
   def test_guest_can_go_to_login_page(self, browser):
      link = MainPageLocators.MAIN_PAGE_LINK

      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
      page = MainPage(browser, link)
      page.open()

      # выполняем метод страницы — переходим на страницу логина
      page.go_to_login_page()
      login_page = LoginPage(browser, browser.current_url)
      login_page.should_be_login_page()

   def test_guest_should_see_login_link(self, browser):
      link = MainPageLocators.MAIN_PAGE_LINK
      page = MainPage(browser, link)
      page.open()
      page.should_be_login_link()

def test_guest_should_see_login_page(browser):
   link = LoginPageLocators.LOGIN_PAGE_LINK
   page = LoginPage(browser, link)
   page.open()
   page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
   link = MainPageLocators.MAIN_PAGE_LINK

   page = MainPage(browser, link)
   page.open()

   page.go_to_basket_page()
   cart_page = BasketPage(browser, browser.current_url)
   # проверка, что корзина пустая
   cart_page.should_be_cart_is_empty()
