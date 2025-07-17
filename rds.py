import csv
import re

from fetch import fetch_page_content
from config import RDS_URL, DATA_DIR
from classes import Optic

pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)")

def collect_red_dots():
    content = fetch_page_content(RDS_URL)
    rds_rows = content.find_all('td', class_='list-td')
    print(f"Found {len(rds_rows)} rows")

    red_dot_list = []
    for row in rds_rows:
        title_div = row.find('div', class_='list-title')
        strong_tag = title_div.find("strong")
        name = strong_tag.get_text(strip=True) if strong_tag else title_div.get_text(strip=True)

        feature_div = row.find('div', class_='list-features-2')
        raw_desc = feature_div.text.strip() if feature_div else "N/A"

        matches = pattern.findall(raw_desc)
        height = 'N/A'
        weight = 'N/A'
        for match in matches:
            value = match[0]
            unit = match[1]
            if unit == 'in':
                height = value if value else height
            elif unit == 'oz':
                weight = value if value else weight

        rds = Optic(
            name=name,
            height=height,
            weight=weight,
            raw_desc=raw_desc,
            optic_type="rds"
        )
        red_dot_list.append(rds)

    if not red_dot_list:
        print("No red dots found")
        return

    keep_list = [rds for rds in red_dot_list if "DISCONTINUED" not in rds.name]
    headers = list(vars(keep_list[0]).keys())
    save_path = DATA_DIR / "red_dot_sights.csv"

    try:
        with open(save_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows([vars(rds) for rds in keep_list])
        print(f"Successfully wrote red dot sights to CSV: {save_path}")
    except IOError as e:
        print(f"I/O Error: {e}")



if __name__ == '__main__':
    collect_red_dots()