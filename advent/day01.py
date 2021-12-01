from typing import List

TETST_INPUTS = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def get_n_increases(inputs: List[int]) -> int:
    """
    Returns the number of times a value in inputs
    was larger than its predecessor
    """

    deltas = [x - y for x, y in zip(inputs[1:], inputs)]

    return sum([True for x in deltas if x > 0])


def get_n_increases_sum(inputs: List[int]) -> int:
    """
    Returns the number of times a value in inputs
    was larger than its predecessor
    """

    deltas_sums = [(inputs[i] + inputs[i-1] + inputs[i-2]) -
                   (inputs[i-1] + inputs[i-2] + inputs[i-3])
                   for i in range(3, len(inputs))]

    return sum([True for x in deltas_sums if x > 0])


assert get_n_increases(TETST_INPUTS) == 7
assert get_n_increases_sum(TETST_INPUTS) == 5


if __name__ == '__main__':
    with open('inputs/day01.txt') as f:
        inputs = [int(x) for x in f]
        print(get_n_increases(inputs))
        print(get_n_increases_sum(inputs))
