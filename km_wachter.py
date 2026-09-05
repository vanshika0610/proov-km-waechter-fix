# km_wachter.py
# KM-Waechter decides when a Vossberg Mobility car needs a service.
# Written in 2013. Bugs fixed and style modernized 2024.

SERVICE_INTERVAL_KM = 15000
WARN_AT_PERCENT = 80


def wear_percent(km_since_service: float, interval: float) -> float:
    """Return how much of one service interval has been used, as a percentage.

    Uses true (float) division so a car at 14 900 of 15 000 km reads ~99.3 %,
    not 0 % as the old floor-division version produced.
    """
    return (km_since_service / interval) * 100


def needs_service(car: dict) -> bool:
    """Return True if this car has reached or passed the warning threshold.

    A missing 'last_service_km' key means we have no reading — we treat that
    as 'not due' rather than 'never serviced' (which would wrongly flag the car).
    """
    last = car.get("last_service_km")   # None when the key is absent
    if last is None:
        return False
    km_since = car["odometer"] - last
    return wear_percent(km_since, SERVICE_INTERVAL_KM) >= WARN_AT_PERCENT


def check_fleet(fleet: list[dict]) -> list:
    """Flag every car that needs a service and return their IDs."""
    flagged = []
    for car in fleet:
        if needs_service(car):
            flagged.append(car["id"])
            print(f"SERVICE DUE: {car['id']}")
    return flagged
