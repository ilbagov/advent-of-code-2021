from typing import List

INPUTS = ["forward 5", "down 5", "forward 8",
          "up 3", "down 8", "forward 2"]


def get_dive_position(course: List[str]) -> int:
    """
    Calculates the final position of the
    submarine after parsing the description
    of its course
    """

    horiz, depth = 0, 0

    for line in course:
        split_line = line.split(' ')
        direction, _distance = split_line
        distance = int(_distance)

        if direction == 'forward':
            horiz += distance
            continue

        sgn = 1 if direction == 'down' else -1

        depth += sgn*distance

    return horiz*depth


def get_dive_position2(course: List[str]) -> int:
    """
    Calculates the final position of the
    submarine after parsing the description
    of its course using the new approach
    """

    horiz, depth, aim = 0, 0, 0

    for line in course:
        split_line = line.split(' ')
        direction, _distance = split_line
        distance = int(_distance)

        if direction == 'forward':
            horiz += distance
            depth += aim*distance
            continue

        sgn = 1 if direction == 'down' else -1
        aim += sgn*distance

    return horiz*depth


assert get_dive_position(INPUTS) == 150
assert get_dive_position2(INPUTS) == 900

with open('inputs/day02.txt') as f:
    course = [x.strip() for x in f]
    print(get_dive_position(course))
    print(get_dive_position2(course))
