from sage_rat.fetch import fetch_page_content
from sage_rat.config import (
    REF_HOLO_URL,
    refl_holo_pattern,
    SAGE_RAT_OUTPUT_DIR,
    BASIC_CSV_HEADERS
)
from sage_rat.util import (
    collect_height_and_weight,
    collect_name,
    collect_raw_description,
    save_to_csv,
    clean_raw_desc
)


def collect_reflex_and_holo():
    raw_content = fetch_page_content(REF_HOLO_URL)
    content_rows = raw_content.find_all('td', class_='list-td')
    print(f"Found {len(content_rows)} rows")

    holo_rows = []
    for row in content_rows:
        name = collect_name(row)
        raw_desc = collect_raw_description(row)
        height, weight = collect_height_and_weight(raw_desc)

        matches = refl_holo_pattern.findall(raw_desc or "")
        sub_type = matches[0] if matches else "N/A"

        holo_rows.append({
            "name": name,
            "height": height,
            "weight": weight,
            "raw_desc": clean_raw_desc(raw_desc),
            "sub_type": sub_type
        })

    if not holo_rows:
        print("No holographic sights or reflex sights found")
        return

    headers = BASIC_CSV_HEADERS + ["sub_type"]
    save_path = SAGE_RAT_OUTPUT_DIR / "holographic_reflex_sights.csv"
    print(f"Writing content to CSV...")
    save_to_csv(save_path, headers, holo_rows)


if __name__ == '__main__':
    collect_reflex_and_holo()