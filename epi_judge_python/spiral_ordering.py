from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:

    n=len(square_matrix)

    def helper(offset):
        """
        Fill the outer ring at offset

        :param offset:
        :return:
        """

        # if the square is odd sized and we have reached the center then there is only one element
        if offset == n-offset-1:
            return [square_matrix[offset][offset]]

        partial_result = []

        partial_result.extend(square_matrix[offset][offset:~offset])

        for r in range(offset,n-offset-1):
            partial_result.append(square_matrix[r][~offset])

        partial_result.extend(square_matrix[~offset][~offset:offset:-1])

        for r in range(n-offset-1,offset,-1):
            partial_result.append(square_matrix[r][offset])

        return partial_result

    result = []
    for offset in range((n-1)//2+1):
        result += helper(offset)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
