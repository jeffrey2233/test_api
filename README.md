# Test API Project / API 測試專案

<<<<<<< HEAD
This is an **API testing project** using **pytest**. The project tests the [Pixegami Todo API](https://todo.pixegami.io/).
這是一個使用 **pytest** 的 API 測試專案，主要測試 [Pixegami Todo API](https://todo.pixegami.io/)。
=======
API testing project using **pytest**. This project tests the [Pixegami Todo API](https://todo.pixegami.io/) including:
>>>>>>> bdde985ee08120e99b5a4d4d6f0062a20ebca01e

## Features / 功能

* Retrieve a welcome message / 取得歡迎訊息
* Create a task / 建立任務
* Retrieve a task / 取得任務資訊
* Update a task / 更新任務

## Getting Started / 快速開始

### 1. Clone the repository / 下載專案

<<<<<<< HEAD
```bash
git clone https://github.com/jeffrey2233/test_api.git
cd test_api
```

### 2. Create a virtual environment / 建立虛擬環境

```bash
python -m venv .venv
```

### 3. Activate the virtual environment / 啟動虛擬環境

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies / 安裝相依套件

```bash
pip install -r requirements.txt
```

### 5. Run tests with pytest / 執行測試

```bash
pytest
```

## Allure Reports / Allure 報告

Generate Allure reports / 生成 Allure 報告:

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

## Project Structure / 專案結構

```
test_api/
├─ .venv/               # Python virtual environment / Python 虛擬環境
├─ src/                 # Source code (API client, helpers) / 原始程式碼 (API 客戶端、輔助功能)
├─ tests/               # Pytest test cases / 測試案例
├─ requirements.txt     # Project dependencies / 專案相依套件
└─ README.md            # Project documentation / 專案文件
```

## Notes / 注意事項

* API credentials (username, password, base URL) are stored in `settings.ini` or `.env` / API 帳號資訊儲存在 `settings.ini` 或 `.env`
* Use the `APIClient` class in `src/api_client.py` for login and API requests / 使用 `src/api_client.py` 的 `APIClient` 類別進行登入及 API 呼叫
* Tests are flexible and reusable with different accounts / 測試設計可彈性使用不同帳號

## Tips / 小技巧

* Run a single test function / 執行單一測試函數:

```bash
pytest tests/test_auth.py::test_login
```

* For debugging in VSCode, configure `launch.json` with `showReturnValue: true` / 在 VSCode 偵錯時，可在 `launch.json` 設定 `showReturnValue: true` 以顯示回傳值
=======
### 1. Clone the repository
git clone https://github.com/jeffrey2233/test_api.git
cd test_api

### 2. Create a virtual environment
python -m venv .venv

### 3. Activate the virtual environment

Windows:
.venv\Scripts\activate

Linux/macOS:
source .venv/bin/activate

### 4. Install dependencies
pip install -r req.txt

### 5. Run tests with pytest
pytest
>>>>>>> bdde985ee08120e99b5a4d4d6f0062a20ebca01e
