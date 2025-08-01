import re

HOME_URL = "https://sageratsafaris.com/the-optics-database/"
RDS_URL = "https://sageratsafaris.com/micro-red-dot-sights-for-handguns/"
REF_HOLO_URL = "https://sageratsafaris.com/master-list-of-red-dots-and-battle-sights/"
MAGNIF_URL = "https://sageratsafaris.com/master-list-of-magnifiers/"
PRISM_URL = "https://sageratsafaris.com/master-list-of-prism-scopes/"
MOUNTS_URL = "https://sageratsafaris.com/one-piece-rifle-scope-mounts/"
FIXED_POW_URL = "https://sageratsafaris.com/fixed-power-rifle-scopes/"
LPVO_FFP_URL = "https://sageratsafaris.com/master-list-of-first-focal-plane-ffp-illuminated-low-power-variable-optics-lpvos/"
LPVO_SFP_URL = "https://sageratsafaris.com/master-list-of-second-focal-plane-sfp-illuminated-low-power-variable-optics-lpvos/"
MPVO_URL = "https://sageratsafaris.com/master-list-of-all-first-or-front-focal-plane-(ffp)-mid-range-rifle-scopes/"
SHORT_RANGE_HUNT_URL = "https://sageratsafaris.com/master-list-of-short-range-hunting-rifle-scopes/"
LONG_RANGE_HUNT_URL = "https://sageratsafaris.com/master-list-of-long-range-hunting-rifle-scopes-at-least-4-12x/"
ONE_MILE_URL = "https://sageratsafaris.com/one-mile-rifle-scopes/"
LONG_RANGE_FFP = "https://sageratsafaris.com/master-list-ffp-long-range-rifle-scopes/"

URL_LIST = [RDS_URL, REF_HOLO_URL, MAGNIF_URL, PRISM_URL, MOUNTS_URL, FIXED_POW_URL, LPVO_FFP_URL, MPVO_URL]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
SAGE_RAT_OUTPUT_DIR = DATA_DIR / "sage_rat"

RDS = "rds"
OPEN_REFLEX = "open reflex"
CLOSED_REFLEX = "closed reflex"
HOLOGRAPHIC = "holographic"
FIXED_POWER = "fixed power"
LPVO = "LPVO"
MPVO = "MPVO"
MAGNIFIER = "magnifier"
PRISM = "prism"

DOT_GROUP = [RDS, OPEN_REFLEX, CLOSED_REFLEX, HOLOGRAPHIC]
FOV_GROUP = [LPVO, MPVO, MAGNIFIER, FIXED_POWER, PRISM]

BASIC_CSV_HEADERS = ["name", "height", "weight", "raw_desc"]

size_pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)", re.IGNORECASE)
fov_pattern = re.compile(r"FOV ft@100yds:\s*(\d+\.?\d*)", re.IGNORECASE)
refl_holo_pattern = re.compile(r"(Holographic RDS|Open reflex RDS|Closed reflex RDS)", re.IGNORECASE)
mount_pattern = re.compile(r"([\w\s()]+):\s*([\w.-]+)", re.IGNORECASE)
elevation_pattern = re.compile(r"\b(\d{2,3})\s*MOA\s+elev\b", re.IGNORECASE)
