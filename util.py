import re

from bs4 import BeautifulSoup

size_pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)")
fov_pattern = re.compile(r"FOV ft@100yds:\s*(\d+\.?\d*)")
refl_holo_pattern = re.compile(r"(Holographic RDS|Open reflex RDS|Closed reflex RDS)")
mount_pattern = re.compile(r"([\w\s()]+):\s*([\w.-]+)") #key-value pairs


def collect_relevant_content(content: BeautifulSoup | None) -> list:
    if content is None:
        print(f"No content found")
    print("Beginning row collection...")
    rows = content.find_all('td', class_='list-td')
    relevant_rows = []
    content_dict = dict
    for row in rows:
        title_div = row.find('div', class_='list-title')
        feature_div = row.find('div', class_='list-features-2')
        content_dict.update({"title": title_div, "features": feature_div})
        relevant_rows.append(content_dict)

    print(f"Finished collecting relevant content. Count: {len(relevant_rows)}")
    return relevant_rows


# def collect_name(title):


def collect_weight_and_height(raw_desc):
    height = 'N/A'
    weight = 'N/A'
    matches = size_pattern.findall(raw_desc)
    for match in matches:
        value = match[0]
        unit = match[1]
        if unit == 'in':
            height = value if value else height
        elif unit == 'oz':
            weight = value if value else weight

    return height, weight


def parse_optic_table(optics_list, optic_type: str):
    collection = []
    for row in optics_list:
        collector = dict
        title_div = row.find('div', class_='list-title')
        strong_tag = title_div.find("strong")
        name = strong_tag.get_text(strip=True) if strong_tag else title_div.get_text(strip=True)

        feature_div = row.find('div', class_='list-features-2')
        raw_desc = feature_div.text.strip() if feature_div else "N/A"

        height, weight = collect_weight_and_height(raw_desc)

        collector.update({"name": name, "height": height, "weight": weight})
        collection.append(collector)

    print(f"Collected {len(collection)} entries.")
    return collection


def get_fov(raw_desc):
    fov = 'N/A'
    match = fov_pattern.findall(raw_desc)
    if match:
        fov = match[0]

    return fov