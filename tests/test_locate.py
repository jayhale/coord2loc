import pytest

from coord2loc import Coordinate, InvalidCoordinate, locate


@pytest.mark.parametrize(
    "lat,lon",
    [
        # Atlantic Ocean
        (30.0, -40.0),
        (0.0, -30.0),
        # Pacific Ocean
        (0.0, -150.0),
        (30.0, 170.0),
        # Indian Ocean
        (0.0, 80.0),
        (-20.0, 70.0),
        # Arctic Ocean
        (80.0, 0.0),
        (75.0, 180.0),
        # Southern Ocean
        (-60.0, 0.0),
        (-65.0, -60.0),
    ],
)
def test_locate_unknown_locations(lat: float, lon: float):
    coordinate = Coordinate(latitude=lat, longitude=lon)
    location = locate(coordinate)
    assert location is None


@pytest.mark.parametrize(
    "lat,lon",
    [
        (-91, 0),
        (91, 0),
        (0, -181),
        (0, 181),
    ],
)
def test_locate_invalid_coordinate(lat: float, lon: float):
    coordinate = Coordinate(latitude=lat, longitude=lon)
    with pytest.raises(InvalidCoordinate):
        locate(coordinate)
