
from typing import Optional


RAW = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""



class BingoBoard:

    def __init__(self, initial_config: str) -> None:

        board_as_str = [x.split() for x in initial_config.splitlines()]
        self.board = [[int(x) for x in board_row]
                      for board_row in board_as_str]
        self.recognized = [[False for x in board_row]
                           for board_row in self.board]
        self.last_num: Optional[int] = None

    def _check_bingo(self) -> bool:
        """
        Checks if the current board wins the game
        """
        for row in self.recognized:
            if all(row):
                return True

        for n_col in range(5):
            col = [x[n_col] for x in self.recognized]
            if all(col):
                return True

        return False

    def add_number(self, number: int) -> bool:
        """
        Evaluates a new number and checks whether it wins the game
        """
        self.last_num = number
        for row in range(5):
            for col in range(5):
                if self.board[row][col] == number:
                    self.recognized[row][col] = True

        return self._check_bingo()

    def sum_unmarked(self) -> int:
        """
        Sums all unmarked numbers
        """
        total = 0
        for row in range(5):
            for col in range(5):
                if self.recognized[row][col] is False:
                    total += self.board[row][col]
        return total        

    
if __name__ == "__main__":
    input = open("inputs/day04.txt").read()
    bingo_numbers = [int(x) for x in input.splitlines()[0].split(',')]
    initial_configurations = []

    for i in range(2, len(input.splitlines()), 6):
        initial_configurations.append('\n'.join(input.splitlines()[i:i+5]))

    boards = [BingoBoard(initial_config) for initial_config in initial_configurations]

    done = False
    for n in bingo_numbers:
        for b in boards:
            bingo = b.add_number(n)
            if bingo:
                print(b.sum_unmarked())
                print(n*b.sum_unmarked())
                done = True
                break
        if done:
            break
