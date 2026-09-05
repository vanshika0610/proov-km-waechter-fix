# config_loader.py
# Reads settings.cfg.
# Hand-rolled in 2013 because ConfigParser felt "too complicated" at the time.
# Style modernized 2024.

SETTINGS_FILE = "settings.cfg"

KNOWN_KEYS = [
    "service_interval_km",
    "warn_at_percent",
    "report_title",
    "history_file",
    "log_file",
    "mileage_unit",
]


def load_settings(path: str | None = None) -> dict:
    """Load key=value pairs from a .cfg file and return them as a dict.

    Only keys listed in KNOWN_KEYS are kept; unknown keys are silently ignored
    (a typo in the file will never surface — a known limitation of this loader).
    Every value is stored as a string; use get_int() to parse integers.
    """
    if path is None:
        path = SETTINGS_FILE
    settings: dict = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if key in KNOWN_KEYS:
                settings[key] = value
    return settings


def get_int(settings: dict, key: str, fallback: int) -> int:
    """Return settings[key] cast to int, or fallback if the key is absent or non-numeric."""
    if key in settings:
        try:
            return int(settings[key])
        except ValueError:
            return fallback
    return fallback


def get_setting(settings: dict, key: str, fallback: str = "") -> str:
    """Return settings[key], or fallback if the key is absent.

    This is a thin wrapper around dict.get; it existed before dict.get was
    well-known on this team.
    """
    return settings.get(key, fallback)
