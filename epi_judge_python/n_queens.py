from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    """
    Returns all possible placements of non attacking queens on nxn chessboard. The information is
    returned as a list of list where the inner list containes the columns of the queens

    :param n: number of queens
    :return:
    """

    def helper_func(row):
        """
        Tries to places a queen of row. If this is more than the number of queens it means that all
        the queens have been successfully placed so the placements are appended to the master result.
        Otherwise if the placement is valid, the function is called for the next row.
        :param row:
        :return:
        """
        if row==n:
            result.append(col_result.copy())
        else:
            for col in range(n):
                for r,c in enumerate(col_result):
                    if abs(c-col) in (0,row-r):
                        break
                else:
                    col_result.append(col)
                    helper_func(row+1)
                    col_result.pop()

    result=[]
    col_result=[]
    helper_func(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
