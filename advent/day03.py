from collections import defaultdict
from typing import Counter, List

INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split()


def most_common_bits(binary: List[str]) -> str:
    """
    Returns the most common bit in each position from a list
    of binary numbers
    """
    n_bits = len(binary[0])
    most_common = ''

    for pos in range(n_bits):
        bits_at_pos = [x[pos] for x in binary]
        most_common += Counter(bits_at_pos).most_common(1)[0][0]

    return most_common


def power_consumption(binary: List[str]) -> int:
    """
    Calculates gamma*epsilon
    """
    gamma_bin = most_common_bits(binary)
    epsilon_bin = ''.join(['0' if x == '1' else '1' for x in gamma_bin])
    return int(gamma_bin, 2)*int(epsilon_bin, 2)


def count_bits_at_pos(binary: List[str], bin_pos: int) -> defaultdict:
    """
    Returns a dictionary with the bit counts of a given position
    of each binary number in inputted list
    """
    bits_at_pos = [x[bin_pos] for x in binary]
    bit_counter = defaultdict(int)
    for k, v in dict(Counter(bits_at_pos).most_common()).items():
        bit_counter[k] += v
    return bit_counter


def oxy_rating(binary: List[str], bin_pos: int = 0) -> int:
    """
    Calculate the oxygen generator rating
    """
    binary_copy = binary.copy()
    bit_counter = count_bits_at_pos(binary_copy, bin_pos)

    most_common = '1' if bit_counter['1'] >= bit_counter['0'] else '0'
    filtered_numbers = [x for x in binary_copy if x[bin_pos] == most_common]

    if len(filtered_numbers) == 1:
        return int(filtered_numbers[0], 2)

    return oxy_rating(filtered_numbers, bin_pos=bin_pos+1)


def co2_rating(binary: List[str], bin_pos: int = 0) -> int:
    """
    Calculate the oxygen generator rating
    """
    binary_copy = binary.copy()
    bit_counter = count_bits_at_pos(binary_copy, bin_pos)

    least_common = '0' if bit_counter['0'] <= bit_counter['1'] else '1'
    filtered_numbers = [x for x in binary_copy if x[bin_pos] == least_common]
    if len(filtered_numbers) == 1:
        return int(filtered_numbers[0], 2)

    return co2_rating(filtered_numbers, bin_pos=bin_pos+1)


def life_support_rating(binary: List[str]) -> int:
    """
    Multiply the oxygen rating with the co2 rating
    """
    return oxy_rating(binary)*co2_rating(binary)


with open('inputs/day03.txt') as f:
    inputs = [x.strip() for x in f]
    print(power_consumption(inputs))
    print(life_support_rating(inputs))
