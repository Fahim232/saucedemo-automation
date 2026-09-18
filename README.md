# Saucedemo Automation Tests

Automation tests for [https://www.saucedemo.com/](https://www.saucedemo.com/) using **Python + pytest + Selenium WebDriver**, with **Allure** reporting.

## Scenarios Covered

| Test | Description |
|------|-------------|
| Q1 `test_q1_locked_user.py` | Login with `locked_out_user` and verify the lockout error message. |
| Q2 `test_q2_standard_user.py` | Login with `standard_user`, reset App State, add 3 items to cart, go to the final checkout page, verify product names + total price, finish the order, verify the success message, reset App State again and log out. |
| Q3 `test_q3_performance_glitch_user.py` | Login with `performance_glitch_user`, reset App State, filter by name (Z to A), add the first product, go to the final checkout page, verify product name(s) + total price, finish the order, verify the success message, reset App State again and log out. |

## Project Structure

```
saucedemo-automation/
├── conftest.py                 # pytest fixtures + browser options (headed/headless)
├── pytest.ini                  # test discovery + allure-results output
├── requirements.txt
├── run_all.sh                  # run all tests
├── report.sh                   # generate + open the Allure report
├── pages/                      # Page Object Model
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

## Prerequisites

- Python 3.8 or newer
- Google Chrome (or Firefox) installed
- Allure command-line tool
  - macOS: `brew install allure`
  - Other OS: [allure.getxray.app](https://allure.getxray.app/) / follow the [Allure installation guide](https://allurereport.org/docs/install/)

## Setup (first time only)

```bash
cd saucedemo-automation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

Tests run **sequentially** by default. The assignment requires running the
tests **all together** as well as **each one separately** — both commands are
shown below.

> Note: `./.venv/bin/pytest` works without activating the virtual environment
> first. If you activate it (`source .venv/bin/activate`), you can simply use
> `pytest` instead.

### 1. Run ALL three scenarios TOGETHER

```bash
./.venv/bin/pytest tests/
```

or

```bash
./run_all.sh
```

### 2. Run EACH scenario SEPARATELY

```bash
./.venv/bin/pytest tests/test_q1_locked_user.py
./.venv/bin/pytest tests/test_q2_standard_user.py
./.venv/bin/pytest tests/test_q3_performance_glitch_user.py
```

### 3. Optional arguments

```bash
./.venv/bin/pytest tests/ --headed      # run with a visible browser window (default is headless)
./.venv/bin/pytest tests/ --browser firefox
```

### 4. Allure report (after every execution)

An `allure-results` folder is created automatically on **every** test run.

To view the report, open a terminal (activate the venv if needed) and run:

```bash
allure serve allure-results
```

Or generate a static report and open it in the browser:

```bash
./report.sh
```

## GitHub Upload (step by step)

```bash
cd saucedemo-automation
git init
git add .
git commit -m "Saucedemo automation tests (pytest + selenium + allure)"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

> Create an empty **public** repository on GitHub first, then use its URL in the
> `git remote add` command above.

## Troubleshooting

- **Selenium cannot find the browser driver**: upgrade Selenium (`pip install -U selenium`). Selenium 4.6+ auto-manages drivers via Selenium Manager.
- **Slow runs with `performance_glitch_user`**: this user intentionally adds delays. The tests wait up to 90 seconds for the page; a slow run is expected and normal.
- **Report is empty**: make sure `allure-results` contains files after the run (`ls allure-results`).