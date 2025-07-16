import requests
from bs4 import BeautifulSoup

from fetch import fetch_page_content
from config import RDS_URL

def collect_red_dots():
    try:
        content = fetch_page_content(RDS_URL)
        rds_rows = content.find_all('td', class_='list-td')
        print(f"Found {len(rds_rows)} rows")

        for row in rds_rows:
            title_div = row.find('div', class_='list-title')
            name = ''
            if title_div:
                strong_tag = title_div.find('strong')
                if strong_tag:
                    name = strong_tag.text.strip()
            else:
                name = "N/A"

            feature_div = row.find('div', class_='list-features-2')
            raw_desc = feature_div.text.strip() if feature_div else "N/A"


            print(f"\nName: {name}")
            print(f"Raw Description: {raw_desc}")


    except requests.exceptions.RequestException as e:
        print(f"Error fetching {RDS_URL}: error: {e}")