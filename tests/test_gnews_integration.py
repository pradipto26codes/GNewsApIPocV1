import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.gnews_client import search

def test_search_returns_articles():
    data = search("AI", max_results=3)
    assert "articles" in data
    assert len(data["articles"]) > 0
