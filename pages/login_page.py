from selenium.webdriver.common.by import By

from pages.base_page import BasePage

LOGIN_URL = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        super().open(LOGIN_URL)

    def login(self, username, secret):
        self.type(*self.username_input, username)
        self.type(*self.password_input, secret)
        self.click(*self.login_button)

    def get_error(self):
        return self.text(*self.error_message)