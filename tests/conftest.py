import pytest
from src.api_client import APIClient
from src.config import USERNAME, PASSWORD

@pytest.fixture(scope="session")
def api_client():
    client = APIClient()
    client.login(USERNAME, PASSWORD)
    return client