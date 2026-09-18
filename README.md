# Saucedemo Automation

End-to-end UI automation tests for [https://www.saucedemo.com/](https://www.saucedemo.com/) using Python, pytest, Selenium WebDriver and Allure reports.

## Test Scenarios

### Q1 — locked_out_user login

Login with `locked_out_user` and verify the error message: "Sorry, this user has been locked out."

### Q2 — standard_user full purchase

1. Login with `standard_user`.
2. Reset the App State from the hamburger menu.
3. Add 3 items to the cart.
4. Go through checkout up to the final page.
5. Verify the product names and the total price.
6. Finish the purchase and verify the success message.
7. Reset the App State again and log out.

### Q3 — performance_glitch_user full purchase

1. Login with `performance_glitch_user`.
2. Reset the App State from the hamburger menu.
3. Sort products by name (Z to A).
4. Add the first product to the cart.
5. Go through checkout up to the final page.
6. Verify the product name and the total price.
7. Finish the purchase and verify the success message.
8. Reset the App State again and log out.

The total price is checked against the sum of the item prices plus the 8% tax.

## Project Structure

```
saucedemo-automation/
├── conftest.py             # pytest fixtures and browser setup
├── pytest.ini              # test configuration
├── requirements.txt
├── run_all.sh              # runs the whole test suite
├── report.sh               # generates and opens the Allure report
├── pages/                  # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
└── tests/
    ├── test_q1_locked_user.py
    ├── test_q2_standard_user.py
    └── test_q3_performance_glitch_user.py
```

## Getting Started

Requirements:

- Python 3.8 or newer
- Google Chrome or Firefox installed
- Allure command-line tool (macOS: `brew install allure`)

Setup:

```bash
cd saucedemo-automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Tests

The tests run sequentially. Run all of them together, or each one separately.

Run all three scenarios:

```bash
./.venv/bin/pytest tests/
```

Run each scenario separately:

```bash
./.venv/bin/pytest tests/test_q1_locked_user.py
./.venv/bin/pytest tests/test_q2_standard_user.py
./.venv/bin/pytest tests/test_q3_performance_glitch_user.py
```

Extra options:

```bash
./.venv/bin/pytest tests/ --headed       # show the browser window
./.venv/bin/pytest tests/ --browser firefox
```

Note: `performance_glitch_user` intentionally adds delays, so the Q3 test is slower by design.

## Allure Report

An `allure-results` folder is created after every test run. To view the report:

```bash
allure serve allure-results
```

Or use the shortcut:

```bash
./report.sh
```

## Author

Fahim Montasir — [GitHub](https://github.com/Fahim232) · [LinkedIn](https://www.linkedin.com/in/kazifahim-montasir/) · [Portfolio](https://fahim232.github.io)