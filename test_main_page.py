from .pages.main_page import MainPage
from .pages.locators import MainPageLocators, LoginPageLocators
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
   link = MainPageLocators.MAIN_PAGE_LINK
   page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
   page.open()  # открываем страницу
   # login_page = page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
   # login_page.should_be_login_page()
   page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
   login_page = LoginPage(browser, browser.current_url)
   login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
   link = MainPageLocators.MAIN_PAGE_LINK
   page = MainPage(browser, link)
   page.open()
   page.should_be_login_link()

def test_guest_should_see_login_page(browser):
   link = LoginPageLocators.LOGIN_PAGE_LINK
   page = LoginPage(browser, link)
   page.open()
   page.should_be_login_page()