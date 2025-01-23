from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators

class MainPage(BasePage):
    # никаких методов нет, поэтому стави заглушку
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
