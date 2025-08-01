import re

from sage_rat.fetch import fetch_page_content
from sage_rat.config import RDS_URL, SAGE_RAT_OUTPUT_DIR, BASIC_CSV_HEADERS
from sage_rat.util import (
    collect_height_and_weight,
    collect_name,
    collect_raw_description,
    save_to_csv,
    clean_raw_desc
)

pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)")

def collect_red_dots():
    raw_content = fetch_page_content(RDS_URL)
    rds_rows = raw_content.find_all('td', class_='list-td')
    print(f"Found {len(rds_rows)} rows")

    red_dot_list = []
    for row in rds_rows:
        name = collect_name(row)
        raw_desc = collect_raw_description(row)
        height, weight = collect_height_and_weight(raw_desc)

        red_dot_list.append({
            'name': name,
            'height': height,
            'weight': weight,
            'raw_desc': clean_raw_desc(raw_desc),
        })

    if not red_dot_list:
        print("No red dots found")
        return

    keep_list = [rds for rds in red_dot_list if "DISCONTINUED" not in rds['name']]
    headers = BASIC_CSV_HEADERS
    save_path = SAGE_RAT_OUTPUT_DIR / "red_dot_sights.csv"
    save_to_csv(save_path, headers, keep_list)


if __name__ == '__main__':
    collect_red_dots()