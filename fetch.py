import requests
from bs4 import BeautifulSoup
from config import HEADERS

def fetch_page_content(url: str) -> BeautifulSoup | None:
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get content from {url}: {e}")