from typing import List, Tuple


def calculate_slope(coordinate_one: Tuple[float, float], coordinate_two: Tuple[float, float]) -> float:
    x_1, y_1 = coordinate_one
    x_2, y_2 = coordinate_two
    slope = (y_2 - y_1)/(x_2 - x_1)
    return slope

def calculate_slopes(coordinates: List[Tuple[float, float]]) -> List[float]:
    slopes = []

    for i in range(len(coordinates) - 1):
        slope: float = calculate_slope(coordinates[i], coordinates[i+1])
        slopes.append(round(slope, 1))
    return slopes


def find_first_treasure_candidate(coordinates: List[Tuple[float, float]], slope_threshold: float) -> int:
    slopes = calculate_slopes(coordinates)
    for i, slope in enumerate(slopes):
        if slope >= slope_threshold:
            return i + 1
    raise ValueError("No treasure found")
