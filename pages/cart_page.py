from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    checkout_button = (By.ID, "checkout")

    def checkout(self):
        self.click(*self.checkout_button)