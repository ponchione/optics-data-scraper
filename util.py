import re

size_pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)")
fov_pattern = re.compile(r"FOV ft@100yds:\s*(\d+\.?\d*)")
refl_holo_pattern = re.compile(r"(Holographic RDS|Open reflex RDS|Closed reflex RDS)")

def parse_optic_table(optics_list, optic_type: str):
    collector = []
    for row in optics_list:
        title_div = row.find('div', class_='list-title')
        strong_tag = title_div.find("strong")
        name = strong_tag.get_text(strip=True) if strong_tag else title_div.get_text(strip=True)

        feature_div = row.find('div', class_='list-features-2')
        raw_desc = feature_div.text.strip() if feature_div else "N/A"

        height, weight = get_weight_and_height(raw_desc)

        if optic_type == '':
            match = fov_pattern.findall(raw_desc)


def get_weight_and_height(raw_desc):
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

def get_fov(raw_desc):
    fov = 'N/A'
    match = fov_pattern.findall(raw_desc)
    if match:
        fov = match.group(1)
