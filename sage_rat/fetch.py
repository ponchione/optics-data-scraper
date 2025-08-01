import requests
from bs4 import BeautifulSoup
from sage_rat.config import HEADERS

def fetch_page_content(url: str) -> BeautifulSoup | None:
    try:
        print(f"Fetching content...")
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            response.raise_for_status()
        print("Content collected.")
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get content from {url}: {e}")