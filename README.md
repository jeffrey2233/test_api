# DummyJSON API Testing Project

This is an **API testing project** using **pytest**. The project tests the [DummyJSON API](https://dummyjson.com/) and demonstrates automated API testing including login, data retrieval, and payload manipulation.

## Features

* Login with username and password
* Retrieve user information (`/auth/me`)
* Fetch lists of users, products, or other DummyJSON endpoints
* Send custom POST/GET requests and handle payloads

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/jeffrey2233/test_api.git
cd test_api
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Tests with Pytest

```bash
pytest
```

This will automatically discover and run all tests in the `tests/` directory.

## Allure Reports

Generate Allure reports to visualize test results:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Project Structure

```
test_api/
├─ .venv/               # Python virtual environment
├─ src/                 # Source code (API client, helpers)
├─ tests/               # Pytest test cases
├─ requirements.txt     # Project dependencies
├─ settings.ini         # API credentials and base URL
└─ README.md            # Project documentation
```

## Notes

* API credentials (username, password, base URL) are stored in `settings.ini` or `.env`.
* Use the `APIClient` class in `src/api_client.py` to handle login and API requests.
* Tests are designed to be flexible and reusable with different DummyJSON accounts.

## Tips

* Run a single test function:

```bash
pytest tests/test_auth.py::test_login
```

* For debugging in VSCode, configure `launch.json` with `showReturnValue: true`.
