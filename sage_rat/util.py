import csv
import re
from pathlib import Path

size_pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)")
fov_pattern = re.compile(r"FOV ft@100yds:\s*(\d+\.?\d*)")
refl_holo_pattern = re.compile(r"(Holographic RDS|Open reflex RDS|Closed reflex RDS)")
mount_pattern = re.compile(r"([\w\s()]+):\s*([\w.-]+)")


def clean_raw_desc(raw_desc):
    return raw_desc.strip().removeprefix("Features: ")


def collect_content(raw_content):
    content_rows = raw_content.find_all('td', class_='list-td')
    print(f"Found {len(content_rows)} rows")


def collect_name(content_row):
    title_div = content_row.find('div', class_='list-title')
    strong_tag = title_div.find('strong')
    name = strong_tag.get_text(strip=True) if strong_tag else title_div.get_text(strip=True)
    return name


def collect_raw_description(content_row):
    feature_div = content_row.find('div', class_='list-features-2')
    raw_desc = feature_div.text.strip() if feature_div else "N/A"
    return raw_desc


def collect_height_and_weight(raw_desc):
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
        fov = match[0]

    return fov


def save_to_csv(save_path: Path, headers, content: list[dict]):
    if headers is None:
        raise ValueError("Headers must not be None")

    if content is None or len(content) == 0:
        raise ValueError("Content must not be None")

    try:
        with open(save_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(content)
        print(f"Successfully wrote content rows to CSV: {save_path}")
    except IOError as e:
        print(f"I/O Error: {e}")