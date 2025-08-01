import csv

from config import HOME_URL, SAGE_RAT_OUTPUT_DIR
from fetch import fetch_page_content
from typing import Dict, List


def collect_manufacturers_and_oems():
    content = fetch_page_content(HOME_URL)
    all_tables = content.find_all("table")

    scrape_targets = {
        'Brand': 'brands_with_counts.csv',
        'OEM': 'oems_with_counts.csv',
    }

    for name_type, filename in scrape_targets.items():
        for table in all_tables:
            head = table.find("thead")
            if head and name_type in head.text:
                print(f"Found {name_type} in table. Processing...")
                table_body = table.find("tbody")
                data_dict = collect_name_and_count(table_body)
                save_list = build_save_list(data_dict, name_type)
                headers = [name_type, "Count"]
                write_to_csv(filename, headers, save_list)
                break


def collect_name_and_count(table_body) -> Dict[str, str]:
    data = dict()
    rows = table_body.find_all("tr")

    for row in rows:
        cells = row.find_all("td")

        if len(cells) < 2:
            continue

        name_cell = cells[0]
        strong_tag = name_cell.find("strong")
        name = strong_tag.get_text(strip=True) if strong_tag else name_cell.get_text(strip=True)

        count = cells[1].get_text(strip=True).replace(',', '')
        data[name] = count

    return data


def build_save_list(data: Dict[str, str], name_header: str) -> List[Dict[str, str]]:
    list_for_csv = []
    for name, count in data.items():
        list_for_csv.append({name_header: name, "Count": count})
    return list_for_csv


def write_to_csv(file_name: str, headers: List[str], save_list: List[Dict[str, str]]) -> None:
    save_path = SAGE_RAT_OUTPUT_DIR / file_name
    try:
        with open(save_path, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(save_list)
        print(f"Successfully wrote data to {save_path}")
    except ValueError as e:
        print(f"ERROR writing to {file_name}: {e}")
        print(f"Headers: {headers}")
        if save_list:
            print(f"First data row keys: {save_list[0].keys()}")



if __name__ == '__main__':
    collect_manufacturers_and_oems()