import requests

GNEWS_API_KEY = "1a186ded5e95586529ac77e0afc3274b"

GNEWS_URL = "https://gnews.io/api/v4/search"


def search(query, token=GNEWS_API_KEY, max_results=10):
    """Search GNews for `query`. Uses hardcoded API key unless overridden."""
    if not token:
        raise RuntimeError("GNEWS_API_KEY not set")
    params = {"q": query, "token": token, "max": max_results}
    resp = requests.get(GNEWS_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
