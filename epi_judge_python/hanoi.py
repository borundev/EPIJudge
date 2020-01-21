import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:

    def hanoi_tower_helper(nr,initial_peg, final_peg, use_peg):
        if nr>0:

            # move the top nr-1 disks from the initial peg to the use peg
            hanoi_tower_helper(nr-1,initial_peg,use_peg,final_peg)

            # move the last peg to the final one and record that move
            pegs[final_peg].append(pegs[initial_peg].pop())
            result.append([initial_peg,final_peg])

            # move the nr-1 disks moved earlier to the use peg to the final peg
            hanoi_tower_helper(nr - 1, use_peg, final_peg, initial_peg)

    result =[]

    # initialize the pegs with all the disks on the first one
    pegs = [list(reversed(range(1,num_rings+1)))] + [[] for _ in range(1,NUM_PEGS)]

    hanoi_tower_helper(num_rings,0,1,2)

    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
