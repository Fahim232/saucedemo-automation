import allure
import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PERFORMANCE_GLITCH_USER = "performance_glitch_user"
PASSWORD = "secret_sauce"

SUCCESS_MESSAGE = "Thank you for your order!"


@allure.title("Q3 - performance_glitch_user purchase with Z to A sort")
@allure.feature("Purchase journey")
@pytest.mark.q3
def test_performance_glitch_user_full_purchase_journey(driver):
    with allure.step("Log in with performance_glitch_user"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(PERFORMANCE_GLITCH_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    with allure.step("Reset the App State from the hamburger menu"):
        inventory_page.reset_app_state()

    with allure.step("Filter products by name (Z to A)"):
        inventory_page.sort_name_z_to_a()
        names = inventory_page.get_item_names()
        assert names == sorted(names, reverse=True)

    with allure.step("Add the first product to the cart"):
        first_product = inventory_page.get_first_item_name()
        inventory_page.add_to_cart(first_product)

    with allure.step("Open the cart and start checkout"):
        inventory_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.checkout()

    checkout_page = CheckoutPage(driver)

    with allure.step("Fill in checkout details"):
        checkout_page.fill_info("Fahim", "montasir", "Dhaka -1212")

    with allure.step("Verify the product name on the final checkout page"):
        assert checkout_page.get_item_names() == [first_product]

    with allure.step("Verify the total price on the final checkout page"):
        prices = checkout_page.get_item_prices()
        assert checkout_page.get_total() == checkout_page.expected_total(prices)

    with allure.step("Finish the purchase"):
        checkout_page.finish()

    with allure.step("Verify the successful order message"):
        assert checkout_page.success_message == SUCCESS_MESSAGE

    with allure.step("Return home, reset the App State and log out"):
        checkout_page.back_home()
        inventory_page.reset_app_state()
        inventory_page.logout()

    with allure.step("Verify we are back on the login page"):
        assert "saucedemo.com" in driver.current_url