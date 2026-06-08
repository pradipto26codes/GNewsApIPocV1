import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from gnews_client import search


def print_articles(data):
    articles = data.get("articles", [])
    print(f"Found {len(articles)} articles")
    for index, article in enumerate(articles, start=1):
        print("\n" + "=" * 40)
        print(f"Article {index}")
        print(f"Title: {article.get('title')}")
        print(f"Source: {article.get('source', {}).get('name')}")
        print(f"Published: {article.get('publishedAt')}")
        print(f"Description: {article.get('description')}")
        print(f"URL: {article.get('url')}")
        print("=" * 40)


def main():
    query = "News about AI"
    print(f"Searching GNews for '{query}'...")
    data = search(query, max_results=5)
    print_articles(data)


if __name__ == "__main__":
    main()
