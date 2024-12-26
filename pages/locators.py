from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.ID, "login_link")

class LoginPageLocators():
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"
    SUBSTRING_URL_ON_LOGIN_PAGE = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    PRODUCT_PAGE_PROMO = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear
    BOOK_NAME_ON_PAGE_STORE = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE_ON_PAGE_STORE = (By.CLASS_NAME, "price_color")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME_ON_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BOOK_PRICE_ON_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")