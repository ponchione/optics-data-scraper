import requests
from bs4 import BeautifulSoup

from fetch import fetch_page_content
from config import LPVO_SFP_URL, HEADERS


def collect_sfp_lpvo():
    response = requests.get(LPVO_SFP_URL, headers=HEADERS, timeout=10)
    if response.status_code != 200:
        response.raise_for_status()
    content = BeautifulSoup(response.content, "lxml")
    tables = content.find_all("table")
    my_table = tables[0]
    rows = my_table.select('tr[class~="list-tr"]')

    print(f"Rows: {len(rows)}")

if __name__ == "__main__":
    collect_sfp_lpvo()