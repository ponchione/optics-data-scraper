from sage_rat.fetch import fetch_page_content
from sage_rat.config import (
    LONG_RANGE_FFP,
    SAGE_RAT_OUTPUT_DIR,
    BASIC_CSV_HEADERS,
    elevation_pattern, fov_pattern
)
from sage_rat.util import (
    collect_height_and_weight,
    collect_name,
    collect_raw_description,
    save_to_csv,
    clean_raw_desc
)

def collect_long_range_ffp__sights():
    raw_content = fetch_page_content(LONG_RANGE_FFP)
    rds_rows = raw_content.find_all('td', class_='list-td')
    print(f"Found {len(rds_rows)} rows")

    long_ffp_rows = []
    for row in rds_rows:
        name = collect_name(row)
        raw_desc = collect_raw_description(row)
        height, weight = collect_height_and_weight(raw_desc)

        match = fov_pattern.search(raw_desc or "")
        fov = match.group(0) if match else "N/A"

        match = elevation_pattern.search(raw_desc or "")
        elevation = match.group(0) if match else "N/A"

        long_ffp_rows.append({
            'name': name,
            'height': height,
            'weight': weight,
            'raw_desc': clean_raw_desc(raw_desc),
            'fov': fov,
            'elevation': elevation,
        })

    if not long_ffp_rows:
        print("No red dots found")
        return

    headers = BASIC_CSV_HEADERS + ["fov", "elevation"]
    save_path = SAGE_RAT_OUTPUT_DIR / "long_ffp_sights.csv"
    save_to_csv(save_path, headers, long_ffp_rows)


if __name__ == '__main__':
    collect_long_range_ffp__sights()