from typing import List
from collections import Counter
from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    left = 0
    s=set()
    max_val=0
    for right,val in enumerate(A):
        if val in s:
            while A[left] != val and left<right:
                s.remove(A[left])
                left+=1
            left+=1
        s.add(val)
        max_val = max(max_val, right - left + 1)

    return max_val


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
