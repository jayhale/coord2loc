import pytest

from coord2loc import Coordinate, locate


@pytest.mark.parametrize(
    "lat,lon,country,administrative_region",
    [
        # Provinces
        (43.714790, -79.503073, "CAN", "Ontario"),
        (49.2827, -123.1207, "CAN", "British Columbia"),
        (53.8316, -113.4925, "CAN", "Alberta"),
        (52.2388, -106.6771, "CAN", "Saskatchewan"),
        (50.7423, -97.1206, "CAN", "Manitoba"),
        (47.6062, -71.2065, "CAN", "Quebec"),
        (46.4983, -66.1596, "CAN", "New Brunswick"),
        (45.0, -63.0, "CAN", "Nova Scotia"),
        (46.25, -63.0, "CAN", "Prince Edward Island"),
        (53.1355, -57.6604, "CAN", "Newfoundland and Labrador"),
        # Territories
        (63.3447, -136.6673, "CAN", "Yukon"),
        (64.0, -124.0, "CAN", "Northwest Territories"),
        (65.2685, -99.4166, "CAN", "Nunavut"),
    ],
)
def test_locate_usa(lat: float, lon: float, country: str, administrative_region: str):
    coordinate = Coordinate(latitude=lat, longitude=lon)
    location = locate(coordinate)
    assert location.country == country
    assert location.administrative_region == administrative_region
