import allure
import pytest

from pages.login_page import LoginPage

LOCKED_OUT_USER = "locked_out_user"
PASSWORD = "secret_sauce"
EXPECTED_ERROR = "Epic sadface: Sorry, this user has been locked out."


@allure.title("Q1 - Login with locked_out_user shows lockout error")
@allure.feature("Login")
@pytest.mark.q1
def test_locked_out_user_sees_error_message(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOCKED_OUT_USER, PASSWORD)

    with allure.step("Verify the lockout error message is shown"):
        assert login_page.get_error() == EXPECTED_ERROR