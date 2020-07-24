from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:

    """
    We will make a set out of the list and extract an element by element.
    For each element we expand both sides as long as they are in the set, while removing
    those from the set.

    This way the we remove contiguous sequences one by one from the set and keep noting their
    length while at it.

    :param A:
    :return:
    """
    A_set = set(A)
    max_interval_size = 0

    while A_set:
        a=A_set.pop()

        lower_bound=a-1
        while lower_bound in A_set:
            A_set.remove(lower_bound)
            lower_bound-=1

        upper_bound=a+1
        while upper_bound in A_set:
            A_set.remove(upper_bound)
            upper_bound+=1
        max_interval_size = max(max_interval_size,
                                upper_bound-lower_bound-1)

    return max_interval_size


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
