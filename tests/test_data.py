from coord2loc.data import discover


def test_discover():
    results = discover()
    assert len(results) == 2
    assert {"CAN", "USA"} == set(r[0] for r in results)
