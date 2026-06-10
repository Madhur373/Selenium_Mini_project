# Selenium Mini Project

## Overview

This project is a beginner-friendly Selenium automation framework built using Python. The automation script performs an end-to-end test on the SauceDemo website by:

* Logging into the application
* Adding a product to the cart
* Opening the shopping cart
* Verifying the selected product
* Completing the test successfully

This project was created to learn Selenium WebDriver, Python automation, and Git/GitHub workflow.

---

## Tech Stack

* Python 3
* Selenium WebDriver
* Chrome Browser
* WebDriver Manager
* Git & GitHub

---

## Project Structure

```text
Selenium_Mini_Project/
│
├── main.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## Website Used

https://www.saucedemo.com

Test Credentials:

Username: standard_user

Password: secret_sauce

---

## Features

* Automated login
* Product selection
* Add-to-cart functionality
* Cart verification
* Assertion-based validation
* Browser automation using Selenium

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Madhur373/Selenium_Mini_project.git
```

Move into the project directory:

```bash
cd Selenium_Mini_project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Sample Test Flow

1. Open SauceDemo website
2. Enter username and password
3. Login successfully
4. Add Sauce Labs Backpack to cart
5. Open cart
6. Verify product name
7. Display "TEST PASSED"

---

## Future Improvements

* Pytest integration
* Page Object Model (POM)
* Explicit waits
* HTML reports
* Screenshots on failure
* GitHub Actions CI/CD
* Parallel test execution

---

## Author

Madhur Kakkar

GitHub:
https://github.com/Madhur373
