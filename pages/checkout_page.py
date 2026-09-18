from selenium.webdriver.common.by import By

from pages.base_page import BasePage

TAX_RATE = 0.08


class CheckoutPage(BasePage):
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    item_names = (By.CSS_SELECTOR, ".inventory_item_name")
    item_prices = (By.CSS_SELECTOR, ".inventory_item_price")
    total_label = (By.CSS_SELECTOR, "[data-test='total-label']")
    finish_button = (By.ID, "finish")
    complete_header = (By.CSS_SELECTOR, ".complete-header")
    back_home_button = (By.ID, "back-to-products")

    def fill_info(self, name, surname, postcode):
        self.type(*self.first_name, name)
        self.type(*self.last_name, surname)
        self.type(*self.postal_code, postcode)
        self.click(*self.continue_button)

    def get_item_names(self):
        return [element.text for element in self.elements(*self.item_names)]

    def get_item_prices(self):
        return [float(element.text.lstrip("$")) for element in self.elements(*self.item_prices)]

    def get_total(self):
        return float(self.text(*self.total_label).split("$")[1])

    def expected_total(self, prices):
        return round(sum(prices) * (1 + TAX_RATE), 2)

    def finish(self):
        self.click(*self.finish_button)

    @property
    def success_message(self):
        return self.text(*self.complete_header)

    def back_home(self):
        self.click(*self.back_home_button)