# fleet_utils.py
# Catch-all helpers since 2013.
# MILES_PER_KM bug fixed and style modernized 2024.

# 1 km = 0.621371 miles.  The old value (1.609) was miles-to-km, the wrong direction.
MILES_PER_KM = 0.621371


def km_to_miles(km: float) -> float:
    """Convert kilometres to miles.  Used by the nightly UK partner report."""
    return km * MILES_PER_KM


def format_number(value: float) -> str:
    """Format a float to one decimal place."""
    return f"{value:.1f}"


def format_percent(value: float) -> str:
    """Format a float as a whole-number percentage string."""
    return f"{int(value)}%"


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a list of numbers, or 0 if the list is empty.

    statistics.mean has existed since Python 3.4 and could replace this,
    but this function is kept for compatibility with existing callers.
    """
    total = 0.0
    count = 0
    for v in values:
        total += v
        count += 1
    if count == 0:
        return 0
    return total / count


def is_due(pct: float, threshold: float) -> bool:
    """Return True if the wear percentage has reached or passed the threshold."""
    return pct >= threshold


def parse_service_date(text: str) -> tuple | None:
    """Parse a DD.MM.YYYY date string and return (year, month, day), or None if malformed.

    Was needed for the old garage form (2014).  The form no longer exists.
    """
    parts = text.split(".")
    if len(parts) != 3:
        return None
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    return (year, month, day)


def chunk_list(items: list, size: int) -> list[list]:
    """Split a list into chunks of the given size.

    Copied from Stack Overflow in 2013.  No longer called from anywhere.
    """
    chunks = []
    current: list = []
    for item in items:
        current.append(item)
        if len(current) == size:
            chunks.append(current)
            current = []
    if current:
        chunks.append(current)
    return chunks
