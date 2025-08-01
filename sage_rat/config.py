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

URL_AND_TYPE = {
    "rds": RDS_URL,
    "ref_holo": REF_HOLO_URL,
    "magnifier": MAGNIF_URL,
    "prism": PRISM_URL,
    "mount": MOUNTS_URL,
    "fixed_power": FIXED_POW_URL,
    "lvpo_ffp": LPVO_FFP_URL,
    # LPVO_SFP_URL,  URL PAGE CONTENT IS MASSIVELY BROKEN
    "mpvo": MPVO_URL,
    "short_range_hunt": SHORT_RANGE_HUNT_URL,
    "long_range_hunt": LONG_RANGE_HUNT_URL,
    "one_mile": ONE_MILE_URL,
    "long_range_ffp": LONG_RANGE_FFP,
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

from pathlib import Path
ROOT_DIR = Path(__file__).parent.parent
DATA_DIR = ROOT_DIR / "data"
SAGE_RAT_OUTPUT_DIR = DATA_DIR / "sage_rat"

BASIC_CSV_HEADERS = ["type", "name", "raw_desc"]

size_pattern = re.compile(r"(\d+\.?\d*)\s?(in|oz)", re.IGNORECASE)
fov_pattern = re.compile(r"FOV ft@100yds:\s*(\d+\.?\d*)", re.IGNORECASE)
refl_holo_pattern = re.compile(r"(Holographic RDS|Open reflex RDS|Closed reflex RDS)", re.IGNORECASE)
mount_pattern = re.compile(r"([\w\s()]+):\s*([\w.-]+)", re.IGNORECASE)
elevation_pattern = re.compile(r"\b(\d{2,3})\s*MOA\s+elev\b", re.IGNORECASE)
