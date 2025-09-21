def test_login(api_client):
    """Verify that login successfully returns a token"""
    assert api_client.token is not None


def test_get_me(api_client):
    """Verify that GET /auth/me returns the correct username"""
    from src.config import USERNAME  # Get the username from config

    data = api_client.get("/auth/me")  # get() already returns a JSON dict
    assert data.get("username") == USERNAME