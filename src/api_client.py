import requests
from src.config import BASE_URL, USERNAME, PASSWORD


class APIClient:
    def __init__(self, base_url: str = BASE_URL):
        # Initialize base_url, remove trailing slash to avoid duplication
        self.base_url = base_url.rstrip("/")
        # Create requests.Session to keep cookies
        self.session = requests.Session()
        # Token obtained after login
        self.token = None
    
    def login(self, username: str = USERNAME, password: str = PASSWORD):
        login_url = f"{self.base_url}/auth/login"
        payload = {
            "username": username,
            "password": password
        }
        response = self.session.post(login_url, json=payload)
        #If login successful (HTTP 200), extract token and update session header
        if response.status_code == 200:
            data = response.json()
            self.token = data.get("accessToken") #Extract token from response
            # Set Authorization header for future requests
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        return response
    
    def get(self, endpoint: str, **kwargs):
        # Combine base_url and endpoint, ensure only one slash between
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        #lstrip('/') removes leading slash from endpoint

        response = self.session.get(url, **kwargs)
        response.raise_for_status()  # 非 2xx 拋錯
        return response.json()       # ✅ 直接回傳 dict
    
    def post(self, endpoint: str, json: dict = None, **kwargs):
         # Combine base_url and endpoint, ensure only one slash between
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        # lstrip('/') removes leading slash from endpoint
        response = self.session.post(url, json=json, **kwargs)
        response.raise_for_status()
        return response.json()  # 直接回傳 dict