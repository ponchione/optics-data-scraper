from sage_rat.fetch import fetch_page_content
from sage_rat.config import (
    FIXED_POW_URL,
    SAGE_RAT_OUTPUT_DIR,
    BASIC_CSV_HEADERS,
    elevation_pattern
)
from sage_rat.util import (
    collect_height_and_weight,
    collect_name,
    collect_raw_description,
    save_to_csv,
    clean_raw_desc
)

def collect_fixed_power_sights():
    raw_content = fetch_page_content(FIXED_POW_URL)
    rds_rows = raw_content.find_all('td', class_='list-td')
    print(f"Found {len(rds_rows)} rows")

    fixed_rows = []
    for row in rds_rows:
        name = collect_name(row)
        raw_desc = collect_raw_description(row)
        height, weight = collect_height_and_weight(raw_desc)

        match = elevation_pattern.search(raw_desc or "")
        elevation = match.group(0) if match else "N/A"

        fixed_rows.append({
            'name': name,
            'height': height,
            'weight': weight,
            'raw_desc': clean_raw_desc(raw_desc),
            "elevation": elevation,
        })

    if not fixed_rows:
        print("No red dots found")
        return

    headers = BASIC_CSV_HEADERS + ["elevation"]
    save_path = SAGE_RAT_OUTPUT_DIR / "fixed_power.csv"
    save_to_csv(save_path, headers, fixed_rows)


if __name__ == '__main__':
    collect_fixed_power_sights()