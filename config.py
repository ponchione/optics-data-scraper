HOME_URL = "https://sageratsafaris.com/the-optics-database/"
RDS_URL = "https://sageratsafaris.com/micro-red-dot-sights-for-handguns/"
REF_HOLO_URL = "https://sageratsafaris.com/master-list-of-red-dots-and-battle-sights/"
MAGNIF_URL = "https://sageratsafaris.com/master-list-of-magnifiers/"
PRISM_URL = "https://sageratsafaris.com/master-list-of-prism-scopes/"
MOUNTS_URL = "https://sageratsafaris.com/one-piece-rifle-scope-mounts/"
FIXED_POW_URL = "https://sageratsafaris.com/one-piece-rifle-scope-mounts/"
LPVO_FFP_URL = "https://sageratsafaris.com/master-list-of-first-focal-plane-ffp-illuminated-low-power-variable-optics-lpvos/"
LPVO_SFP_URL = "https://sageratsafaris.com/master-list-of-second-focal-plane-sfp-illuminated-low-power-variable-optics-lpvos/"
MPVO_URL = "https://sageratsafaris.com/master-list-of-all-first-or-front-focal-plane-(ffp)-mid-range-rifle-scopes/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

from pathlib import Path
ROOT_DIR = Path(__file__).parent
DATA_DIR = ROOT_DIR / "data"