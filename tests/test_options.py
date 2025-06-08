import pytest

from coord2loc import Coordinate, Options, locate


def test_raise_on_invalid():
    invalid_coordinate = Coordinate(latitude=91, longitude=0)
    options = Options(raise_on_invalid=True)
    with pytest.raises(ValueError):
        locate(invalid_coordinate, options)


def test_none_on_invalid():
    invalid_coordinate = Coordinate(latitude=91, longitude=0)
    options = Options(raise_on_invalid=False)
    assert locate(invalid_coordinate, options) is None


def test_raise_on_not_found():
    unknown_coordinate = Coordinate(latitude=30, longitude=-40)
    options = Options(raise_on_not_found=True)
    with pytest.raises(ValueError):
        locate(unknown_coordinate, options)


def test_none_on_not_found():
    unknown_coordinate = Coordinate(latitude=30, longitude=-40)
    options = Options(raise_on_not_found=False)
    assert locate(unknown_coordinate, options) is None
