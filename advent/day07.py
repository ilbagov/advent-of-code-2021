from typing import List
from math import floor, ceil

RAW = """16,1,2,0,4,2,7,1,2,14"""
TEST_INPUT = [int(x) for x in RAW.split(',')]


def median(xs: List[int]) -> float:
    """
    Calculates the median of a list of ints
    """
    n = len(xs)
    xs_sorted = sorted(xs)
    if n % 2 == 0:
        return 0.5*(xs_sorted[int(n/2)] + xs_sorted[int(n/2-1)])
    else:
        return xs_sorted[int(n/2 + 0.5)]


def mean(xs: List[int]) -> float:
    """
    Calculates the mean of a list of ints
    """
    return sum(xs)/len(xs)


def optimal_fuel_sum(positions: List[int], simple=True) -> int:
    """
    Calculates the optimal fuel needed
    to align the crabs horizontally
    """
    if simple:
        # the minimum of a sum of absolute differences
        # is the median
        med = median(positions)
        fuel = sum(abs(x-med) for x in positions)
    else:
        # the minimum of the fuel in the second case
        # is found at the mean of the position
        opt_point = mean(positions)
        # ceil/floor needed because the coordinates are integers
        fuel = min(0.5*sum(abs(x-ceil(opt_point))**2 + abs(x-ceil(opt_point))
                   for x in positions),
                   0.5*sum(abs(x-floor(opt_point))**2 + abs(x-floor(opt_point))
                   for x in positions))

    return int(fuel)


assert median([1, 2, 3, 4, 2]) == 3
assert median([1, 2, 2, 6, 4, 5]) == 3
assert optimal_fuel_sum(TEST_INPUT) == 37
assert optimal_fuel_sum(TEST_INPUT, simple=False) == 168

if __name__ == "__main__":
    with open("inputs/day07.txt") as f:
        inp = [int(x) for line in f for x in line.split(',')]
    print(optimal_fuel_sum(inp))
    print(optimal_fuel_sum(inp, simple=False))
