from typing import List

from test_framework import generic_test
import random
import operator

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:


    start,end=0,len(A)-1
    comp=operator.gt
    while start<=end:
        pivot_index=random.randint(start,end)
        new_pivot_index=pivot(A, start, end, pivot_index,comp)
        if new_pivot_index==k-1:
            return A[new_pivot_index]
        elif new_pivot_index<k-1:
            start=new_pivot_index+1
        else:
            end=new_pivot_index-1

def pivot(A,start,end,pivot_index,comp):

    # move pivot to the end
    A[pivot_index],A[end]=A[end],A[pivot_index]

    # new_pivot_index will point to the last of the processed elements passing the comp test
    # if none has failed, otherwise it will point at the first that has failed
    new_pivot_index=start

    for i in range(start,end):
        if comp(A[i],A[end]):
            A[new_pivot_index],A[i]=A[i],A[new_pivot_index]
            new_pivot_index+=1
    A[new_pivot_index],A[end]=A[end],A[new_pivot_index]
    return new_pivot_index

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
