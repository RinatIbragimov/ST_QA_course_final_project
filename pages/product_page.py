from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def find_book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_PAGE_STORE).text

    def find_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_PAGE_STORE).text

    def add_book_to_cart(self):
        # находим кнопку и добавляем книгу в корзину
        button_add_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_cart.click()

    def compare_book_and_price_in_store_and_message(self, book_to_compare, price_to_compare):
        self.should_be_right_book_name(book_to_compare)
        self.should_be_right_price_for_book(price_to_compare)

    def should_be_right_book_name(self, book_to_compare):
        # проверка сообщения о добавлении в корзину нужной книги
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME_ON_MESSAGE).text == book_to_compare, "No added book in a cart!"

    def should_be_right_price_for_book(self, price_to_compare):
        # проверка сообщения о цене книги в корзине
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE_ON_MESSAGE).text == price_to_compare, "Wrong price for the book!"