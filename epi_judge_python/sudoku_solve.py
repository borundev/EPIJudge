import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    '''
    Solves a partially filled sudoku. In the bulk of the function we refer to a location by just
    one index i which is related to row and column by i = r * n + c where n is the length of the
    board.

    :param partial_assignment:
    :return:
    '''


    # set the size of the board
    N = len(partial_assignment)
    n = int(math.sqrt(N))

    def get_val(i):
        r, c = i // N, i % N
        return partial_assignment[r][c]

    def set_val(i,val):
        r, c = i // N, i % N
        partial_assignment[r][c] = val

    def allowed_at(i, val):
        r, c = i // N, i % N
        if val in partial_assignment[r]:
            return False
        if val in [partial_assignment[j][c] for j in range(N)]:
            return False

        for _r in range(r // n * n, r // n * n + n):
            for _c in range(c // n * n, c // n * n + n):
                if val == partial_assignment[_r][_c]:
                    return False
        return True


    def helper(i):
        '''
        Try all possible values at location i. If i exceeeds the board size,  it means the board
        is full and return True. If the value at i is not 0, it means that the location is
        already filled so move on to the next location.
        :param i:
        :return:
        '''
        if i == N * N:
            # filled the whole board
            return True

        if get_val(i) != 0:
            # the value if already filled
            return helper(i + 1)

        for val in range(1, N + 1):
            if allowed_at(i, val):
                set_val(i,val)
                result = helper(i + 1)
                if result:
                    # if True has been passed on from above, it means that we have solved the
                    # problem so just pass it on
                    return True
        # if none of the values worked (returned True) that means there was a wrong step earlier,
        # so roll back and return False
        set_val(i,0)
        return False

    return helper(0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
