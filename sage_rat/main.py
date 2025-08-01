import time

import requests
from bs4 import BeautifulSoup

from sage_rat.config import URL_AND_TYPE, SAGE_RAT_OUTPUT_DIR, BASIC_CSV_HEADERS, HEADERS
from sage_rat.util import (
    collect_name,
    collect_raw_description,
    collect_content_rows, save_to_csv
)


def fetch_page_content(url: str) -> BeautifulSoup | None:
    try:
        print(f"Fetching content from {url}")
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            response.raise_for_status()
        print("Content collected.")
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Failed to get content from {url}: {e}")


def fetch_all_raw_data():
    total_count = 0
    raw_data = []

    for opt_type, url in URL_AND_TYPE.items():
        raw_page = fetch_page_content(url)
        raw_rows = raw_page.find_all('td', class_='list-td')
        print(f"Fetched {len(raw_rows)} rows for type: {opt_type}")
        total_count += len(raw_rows)

        for row in raw_rows:
            title_div = row.find('div', class_='list-title')
            strong_tag = title_div.find('strong')
            name = strong_tag.get_text(strip=True) if strong_tag else title_div.get_text(strip=True)

            feature_div = row.find('div', class_='list-features-2')
            raw_desc = feature_div.text.strip() if feature_div else "N/A"

            raw_data.append({
                'type': opt_type,
                'name': name,
                'raw_desc': raw_desc
            })

        if not raw_data:
            print(f"No data found for {opt_type}")

        time.sleep(5)

    print(f"Found {total_count} rows in total")
    save_path = SAGE_RAT_OUTPUT_DIR / "raw_data.csv"
    save_to_csv(save_path, BASIC_CSV_HEADERS, raw_data)
    print(f"Saved all raw data to {save_path}")

if __name__ == "__main__":
    fetch_all_raw_data()