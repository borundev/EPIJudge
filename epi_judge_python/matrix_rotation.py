from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)

    def rotate_layer(offset):
        """
        This is a very straightforward function and the only care needs to be in nothing which
        index goes to which one
        :param offset:
        :return:
        """
        for idx in range(offset,n-1-offset):
            (square_matrix[offset][idx],
            square_matrix[~idx][offset],
            square_matrix[~offset][~idx],
            square_matrix[idx][~offset]) = \
                (square_matrix[~idx][offset],
                square_matrix[~offset][~idx],
                square_matrix[idx][~offset],
                square_matrix[offset][idx])


    for offset in range(n//2):
        rotate_layer(offset)



def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
