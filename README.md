<div align="center">

# 🛒 Saucedemo Automation

**End-to-End UI Automation Tests for [saucedemo.com](https://www.saucedemo.com/)**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-9.x-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Allure](https://img.shields.io/badge/Allure-Reports-CA4848?style=for-the-badge&logo=reportlab&logoColor=white)](https://allurereport.org/)

[![Tests](https://github.com/Fahim232/saucedemo-automation/actions/workflows/ci.yml/badge.svg)](https://github.com/Fahim232/saucedemo-automation/actions/workflows/ci.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/Fahim232/saucedemo-automation?style=for-the-badge&color=blue)](https://github.com/Fahim232/saucedemo-automation/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Fahim232/saucedemo-automation?style=for-the-badge&color=purple)](https://github.com/Fahim232/saucedemo-automation)
[![GitHub stars](https://img.shields.io/github/stars/Fahim232/saucedemo-automation?style=for-the-badge&color=yellow)](https://github.com/Fahim232/saucedemo-automation/stargazers)

A clean **Page Object Model (POM)** based test suite covering login validation and
full purchase journeys on the Sauce Demo demo store, with **Allure** reporting.

</div>

---

## ✅ Test Scenarios

| Q | User | Scenario |
|:-:|:-----|:---------|
| **Q1** | `locked_out_user` | Attempt login → verify the *"Sorry, this user has been locked out."* error message. |
| **Q2** | `standard_user` | Reset App State → add **3 items** to cart → checkout → verify **product names & total price** → finish order → verify **success message** → reset App State → log out. |
| **Q3** | `performance_glitch_user` | Reset App State → filter **Name (Z to A)** → add first product → checkout → verify **product name & total price** → finish order → verify **success message** → reset App State → log out. |

### 🧪 What each test verifies
- ✔️ Locked-out error message display
- ✔️ Item names shown on the order summary match what was added
- ✔️ Total price = sum of item prices + **8% tax** (computed & cross-checked)
- ✔️ "Thank you for your order!" confirmation after finishing purchase
- ✔️ App state reset & logout complete the journey cleanly

---

## 🏗️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Language** | Python |
| **Framework** | pytest |
| **Automation** | Selenium WebDriver (Chrome / Firefox) |
| **Design Pattern** | Page Object Model (POM) |
| **Reporting** | Allure (`allure-pytest`) |
| **CI/CD** | GitHub Actions (see `.github/workflows/ci.yml`) |

---

## 📁 Project Structure

```
saucedemo-automation/
├── .github/workflows/ci.yml   # CI: runs tests + uploads Allure report
├── conftest.py                # pytest fixtures, headed/headless, browser options
├── pytest.ini                 # test discovery + allure-results output
├── requirements.txt
├── run_all.sh                 # run the whole suite
├── report.sh                  # generate + open Allure report
├── pages/                     # Page Object Model
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

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+**
- **Google Chrome** (or Firefox) installed
- **Allure CLI** — macOS: `brew install allure` · other OS: [allurereport.org/docs/install](https://allurereport.org/docs/install/)

### Setup

```bash
cd saucedemo-automation
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ How to Run

Tests run **sequentially**. You can run them all together **or** one by one.

### 1. Run ALL scenarios together

```bash
./.venv/bin/pytest tests/
```
*or, after activating the venv:* `pytest tests/`

### 2. Run each scenario separately

```bash
./.venv/bin/pytest tests/test_q1_locked_user.py
./.venv/bin/pytest tests/test_q2_standard_user.py
./.venv/bin/pytest tests/test_q3_performance_glitch_user.py
```

### 3. Useful options

```bash
./.venv/bin/pytest tests/ --headed         # show the browser window
./.venv/bin/pytest tests/ --browser firefox
./run_all.sh                               # shortcut for running all tests
```

> 💡 `performance_glitch_user` intentionally adds network delays, so Q3 is
> slower by design — that's expected.

---

## 📊 Allure Report

`allure-results/` is generated automatically on **every** run.

### Live view

```bash
allure serve allure-results
```

### Static report

```bash
./report.sh
```

The report shows each scenario with step-by-step breakdown, status, and timings.

---

## 🤖 CI/CD

A [GitHub Actions workflow](.github/workflows/ci.yml) runs the full suite on every
push. The "Tests passing" badge above reflects the latest CI run, and the Allure
report is uploaded as a build artifact.

---

## 👤 Author

**Kazi Fahim (Fahim Montasir)**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Fahim232)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kazifahim-montasir/)
[![Portfolio](https://img.shields.io/badge/Portfolio-8B5CF6?style=for-the-badge&logo=google-chrome&logoColor=white)](https://fahim232.github.io)

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Fahim232">Fahim Montasir</a> · Software Quality Assurance Engineer (in progress 🚀)
</div>