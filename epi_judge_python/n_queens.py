from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:

    def helper(row):

        if row==n:
            results.append(partial_results.copy())
            return

        for col in range(n):
            if not any([abs(c-col) in (0,row-r) for r,c in enumerate(partial_results)]):
                partial_results.append(col)
                helper(row+1)
                partial_results.pop()

    results =[]
    partial_results=[]
    helper(0)
    return results


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
