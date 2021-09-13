import pytest


@pytest.mark.parametrize("first_coordinate, second_coordinate, x_val, expected", [
    ((0, 0), (6, 6), 3, 3),
    ((2, 4), (6, 0), 4, 2)])
def test_coordinate_calc(first_coordinate, second_coordinate, x_val, expected):
    from coordinate_plane import coordinate_calc
    answer = coordinate_calc(first_coordinate, second_coordinate, x_val)
    assert answer == expected
