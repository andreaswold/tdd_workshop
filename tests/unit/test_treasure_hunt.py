from typing import List
from tdd_workshop.treasure_hunt import calculate_slopes, find_first_treasure_candidate


def test_correctly_calculated_slopes():

    coordinates = [(1, 1), (2.0, 1.8), (2.5, 2.1), (3, 2), (4.3, 7.2), (5.3, 6.2)]
    expected_slopes = [0.8, 0.6, -0.2, 4.0, -1.0]

    slopes: List[float] = calculate_slopes(coordinates)

    assert slopes == expected_slopes

def test_find_first_coordinate_with_slope_over_threshold():
    coordinates = [(1, 1), (2.0, 1.8), (2.5, 2.1), (3, 2), (4.3, 7.2), (5.3, 6.2)]
    index_with_treasure: int = find_first_treasure_candidate(coordinates, 1)

    expected_index = 4
    assert index_with_treasure == expected_index
