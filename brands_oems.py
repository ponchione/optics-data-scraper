from config import HOME_URL
from fetch import fetch_page_content
from typing import Dict

def collect_manufacturers_and_oems():
    content = fetch_page_content(HOME_URL)
    all_tables = content.find_all("table")
    brands = dict()
    oems = dict()
    for table in all_tables:
        head = table.find("thead")
        if 'Brand' in head.text:
            brands = collect_name_and_count(table)
        if 'OEM' in head.text:
            oems = collect_name_and_count(table)

    print(f"{len(brands)} brands and {len(oems)} OEMs")


def collect_name_and_count(table) -> Dict[str, int]:
    data = dict()
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        name_cell = cells[0]
        strong_tag = name_cell.find("strong")
        name = strong_tag.get_text(strip=True) if strong_tag else name_cell.get_text(strip=True)
        count = cells[1].get_text(strip=True)
        data.update({name: count})
    return data

if __name__ == '__main__':
    collect_manufacturers_and_oems()