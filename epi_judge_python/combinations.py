from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:

    """
    Return nCk elements from (1...n). Note that compared to standard problems this is not (0.. n-1)
    so a little care is required
    :param n:
    :param k:
    :return: List of lists of integers of choice of k intergers from 1 to n
    """

    def combinations_helper(item):
        """
        Helper function that works onward from item number.

        :param item:
        :param partial_result:
        :return:
        """
        remaining=k-len(partial_result)
        if not remaining:
            result.append(partial_result.copy())
            return

        for x in range(item,n+1):

            # save extra computation if there are not gonna be enough remaining
            if n-x < remaining-1:
                break

            partial_result.append(x)
            combinations_helper(x+1)
            partial_result.pop() # backtrack

    result: List[List[int]] = []
    partial_result: List[int] = []
    combinations_helper(1)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
