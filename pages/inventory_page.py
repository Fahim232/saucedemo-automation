from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage

INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


class InventoryPage(BasePage):
    burger_menu = (By.ID, "react-burger-menu-btn")
    sidebar_close = (By.ID, "react-burger-cross-btn")
    menu_wrap = (By.CSS_SELECTOR, ".bm-menu-wrap")
    reset_link = (By.ID, "reset_sidebar_link")
    logout_link = (By.ID, "logout_sidebar_link")
    sort_container = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    item_names = (By.CSS_SELECTOR, ".inventory_item_name")
    cart_link = (By.CSS_SELECTOR, ".shopping_cart_link")

    def open(self):
        super().open(INVENTORY_URL)

    def reset_app_state(self):
        self._open_menu()
        self.click(*self.reset_link)
        self._close_sidebar()

    def logout(self):
        self._open_menu()
        self.click(*self.logout_link)

    def sort_name_z_to_a(self):
        Select(self.find(*self.sort_container)).select_by_value("za")

    def get_item_names(self):
        return [element.text for element in self.elements(*self.item_names)]

    def get_first_item_name(self):
        return self.elements(*self.item_names)[0].text

    def add_to_cart(self, product_name):
        button_id = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        self.click(By.ID, button_id)

    def go_to_cart(self):
        self.click(*self.cart_link)
        self.wait.until(lambda driver: "cart.html" in driver.current_url)

    def _open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.burger_menu))
        self.click(*self.burger_menu)
        self.wait.until(
            lambda driver: driver.find_element(*self.menu_wrap).get_attribute("aria-hidden") == "false"
        )

    def _close_sidebar(self):
        close_button = self.find(*self.sidebar_close)
        if close_button.is_displayed():
            self.click(*self.sidebar_close)
        self.wait.until(
            lambda driver: "translate3d(-100%" in driver.find_element(*self.menu_wrap).get_attribute("style")
        )