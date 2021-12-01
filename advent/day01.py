from typing import List

TETST_INPUTS = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def get_n_increases(inputs: List[int]) -> int:
    """
    Returns the number of times a value in inputs
    was larger than its predecessor
    """
    return sum([((n_2 - n_1) > 0) for n_2, n_1 in zip(inputs[1:], inputs)])


def get_n_increases_sum(inputs: List[int]) -> int:
    """
    Returns the number of times a sliding window sum
    of length 3 of elements of inputs was larger
    than the previous sliding window sum 
    """
    return sum([((n_4 + n_3 + n_2) > (n_3 + n_2 + n_1))
               for n_4, n_3, n_2, n_1
               in zip(inputs[3:], inputs[2:], inputs[1:], inputs)])


assert get_n_increases(TETST_INPUTS) == 7
assert get_n_increases_sum(TETST_INPUTS) == 5


if __name__ == '__main__':
    with open('inputs/day01.txt') as f:
        inputs = [int(x) for x in f]
        print(get_n_increases(inputs))
        print(get_n_increases_sum(inputs))
