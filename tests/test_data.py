from coord2loc.data import discover


def test_discover():
    results = discover()
    assert len(results) == 1
    assert results[0][0] == "USA"
