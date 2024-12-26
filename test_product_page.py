import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

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
    page.compare_book_and_price_in_store_and_message(book_name_on_page, book_price_on_page)