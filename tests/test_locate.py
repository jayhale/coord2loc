import pytest

from coord2loc import Coordinate, InvalidCoordinate, locate


@pytest.mark.parametrize(
    "lat,lon,country,administrative_region",
    [
        (32.806671, -86.791130, "USA", "Alabama"),
        (61.370716, -152.404419, "USA", "Alaska"),
        (33.729759, -111.431221, "USA", "Arizona"),
        (34.969704, -92.373123, "USA", "Arkansas"),
        (36.116203, -119.681564, "USA", "California"),
        (39.059811, -105.311104, "USA", "Colorado"),
        (41.597782, -72.755371, "USA", "Connecticut"),
        (39.318523, -75.507141, "USA", "Delaware"),
        (38.897438, -77.026817, "USA", "District of Columbia"),
        (27.766279, -81.686783, "USA", "Florida"),
        (33.040619, -83.643074, "USA", "Georgia"),
        (19.584189, -155.454296, "USA", "Hawaii"),
        (44.240459, -114.478828, "USA", "Idaho"),
        (40.349457, -88.986137, "USA", "Illinois"),
        (39.849426, -86.258278, "USA", "Indiana"),
        (42.011539, -93.210526, "USA", "Iowa"),
        (38.526600, -96.726486, "USA", "Kansas"),
        (37.668140, -84.670067, "USA", "Kentucky"),
        (31.169546, -91.867805, "USA", "Louisiana"),
        (44.693947, -69.381927, "USA", "Maine"),
        (39.063946, -76.802101, "USA", "Maryland"),
        (42.230171, -71.530106, "USA", "Massachusetts"),
        (43.326618, -84.536095, "USA", "Michigan"),
        (45.694454, -93.900192, "USA", "Minnesota"),
        (32.741646, -89.678696, "USA", "Mississippi"),
        (38.456085, -92.288368, "USA", "Missouri"),
        (46.921925, -110.454353, "USA", "Montana"),
        (41.125370, -98.268082, "USA", "Nebraska"),
        (38.313515, -117.055374, "USA", "Nevada"),
        (43.452492, -71.563896, "USA", "New Hampshire"),
        (40.298904, -74.521011, "USA", "New Jersey"),
        (34.840515, -106.248482, "USA", "New Mexico"),
        (42.165726, -74.948051, "USA", "New York"),
        (35.630066, -79.806419, "USA", "North Carolina"),
        (47.528912, -99.784012, "USA", "North Dakota"),
        (40.388783, -82.764915, "USA", "Ohio"),
        (35.565342, -96.928917, "USA", "Oklahoma"),
        (44.572021, -122.070938, "USA", "Oregon"),
        (40.590752, -77.209755, "USA", "Pennsylvania"),
        (41.680893, -71.511780, "USA", "Rhode Island"),
        (33.856892, -80.945007, "USA", "South Carolina"),
        (44.299782, -99.438828, "USA", "South Dakota"),
        (35.747845, -86.692345, "USA", "Tennessee"),
        (31.054487, -97.563461, "USA", "Texas"),
        (40.150032, -111.862434, "USA", "Utah"),
        (44.045876, -72.710686, "USA", "Vermont"),
        (37.769337, -78.169968, "USA", "Virginia"),
        (47.400902, -121.490494, "USA", "Washington"),
        (38.491226, -80.954453, "USA", "West Virginia"),
        (44.268543, -89.616508, "USA", "Wisconsin"),
        (42.755966, -107.302490, "USA", "Wyoming"),
    ],
)
def test_locate_known_locations(
    lat: float, lon: float, country: str, administrative_region: str
):
    coordinate = Coordinate(latitude=lat, longitude=lon)
    location = locate(coordinate)
    assert location.country == country
    assert location.administrative_region == administrative_region


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
