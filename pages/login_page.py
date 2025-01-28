from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка, что в адресе есть "login"
        assert LoginPageLocators.SUBSTRING_URL_LOGIN in self.browser.current_url, \
            "No 'login' in url on this page!"

    def should_be_login_form(self):
        # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            "Registration form is not presented"

    def make_email_and_password(self):
        # генерация почты и передача пароля
        return (str(time.time()) + "@fakemail.org", "Testing_passwod_1230")

    def register_new_user(self, test_email, test_password):
        # регистрация нового пользователя

        # находим элементы на странице: поля ввода почты, пароля и кнопку регистрации
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_INPUT)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        pass_confirm = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        # вводим почту и пароль
        email_input.send_keys(test_email)
        pass_input.send_keys(test_password)
        pass_confirm.send_keys(test_password)

        # нажимаем на кнопку: зарегистрировать
        registration_button.click()
