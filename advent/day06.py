from typing import List

RAW = """3,4,3,1,2"""
TEST_STATE = [int(x) for x in RAW.split(',')]


def simulate_fish_growth(init_state: List[int], n_days: int) -> int:
    """
    Use a counts dictionary, otherwise complexity would be too high.
    """
    coutner_dict = {k: init_state.count(k) for k in range(10)}
    n_zeros = coutner_dict[0]

    for i in range(n_days):
        # add new fish if there are any 0's in the state
        coutner_dict[7] += coutner_dict[0]
        coutner_dict[0] = 0
        coutner_dict[9] += n_zeros
        # decrement timers by 1
        for n in range(1, 10):
            if coutner_dict[n] > 0:
                coutner_dict[n-1] = coutner_dict[n]
                coutner_dict[n] = 0
        # get number of timers which are at 0
        n_zeros = coutner_dict[0]

    return sum(coutner_dict.values())


assert (simulate_fish_growth(TEST_STATE, 80)) == 5934
assert (simulate_fish_growth(TEST_STATE, 256)) == 26984457539


if __name__ == "__main__":
    inputs = open("inputs/day06.txt").read()
    init_state = [int(x) for x in inputs.split(',')]
    print((simulate_fish_growth(init_state, 80)))
    print((simulate_fish_growth(init_state, 256)))
