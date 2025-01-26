from .base_page import BasePage
from .locators import CartPageLocators

class BasketPage(BasePage):
    def should_be_cart_is_empty(self):
        substring = CartPageLocators.SUBSTRING_BASKET_IS_EMPTY_EN_GB
        # проверка, что на странице присутствует строчка о пустой корзине
        assert substring in self.browser.find_element(*CartPageLocators.BASKET_EMPTY).text, \
            "No message of empty basket!"
