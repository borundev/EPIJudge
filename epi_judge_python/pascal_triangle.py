from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n==0:
        return []
    all_data=[[1]]
    for i in range(n-1):
        new_data=[1]
        for k in range(len(all_data[-1])-1):
            new_data.append(all_data[-1][k]+all_data[-1][k+1])
        new_data.append(1)
        all_data.append(new_data)
    return all_data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
