from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
    SUBSTRING_LOGIN = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")