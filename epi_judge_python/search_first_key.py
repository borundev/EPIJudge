from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    start,end=0,len(A)-1
    result=-1
    while start <= end:
        mid = start + (end-start)//2
        if A[mid]<k:
            start=mid+1
        elif A[mid]>k:
            end=mid-1
        else:

            # if we have a match we note the position and still search on its left using binary
            # search

            A[mid]==k
            result=mid
            end=mid-1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
