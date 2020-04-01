import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:

    pivot_val=A[pivot_index]

    equal_start=0
    unassigned_start=0
    bigger_start=len(A)

    # the smaller ones will be in A[:equal_start]
    # the ones equal to pivot will be in A[equal_start:unassigned_start]
    # the unassigned ones will be in A[unassigned_start:bigger_start]
    # the ones bigger will be in A[bigger_start:]

    # Invariants
    # so equal_start is pointing at the first of the equal_to_pivot
    # unassigned_start is pointing to the first of unassigned
    # bigger_start is pointing to the first of the bigger


    # at each step in the loop, the unassigned region shrinks
    # either from unassigned_start+=1 or bigger_start-=1

    while unassigned_start<bigger_start:
        if A[unassigned_start]<pivot_val:
            # exchange the unassigned start with the equal start
            A[unassigned_start],A[equal_start]=A[equal_start],A[unassigned_start]
            # now the equal start has an element less than the pivot
            # while the unassigned start has an element equal to the pivot

            # So we adjust the values of equal_start and unassigned start to
            # be consistent with the new state of affairs
            equal_start+=1
            unassigned_start += 1

        elif A[unassigned_start]>pivot_val:
            # exchanged the unassigned start with the unassigned end
            A[unassigned_start],A[bigger_start-1]=A[bigger_start-1],A[unassigned_start]
            # now the unassigned end is bigger than the pivot
            # however the unassigned beginning is still unassigned

            # So we adjust _only_ the values of bigger_start to be
            # consistent with the new state of affair
            bigger_start -= 1
        else:
            # The unassigned_start turns out to be equal to the pivot
            # So we adjust the unassigned start to be consistent
            # with the new state of affairs
            unassigned_start+=1
    return

def dutch_flag_partition_On_v2(pivot_index, A):
    pivot = A[pivot_index]

    smaller,equal,larger=0,0,len(A)
    while equal<larger:

        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller+=1
            equal+=1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger-=1
            A[equal], A[larger] = A[larger], A[equal]


dutch_flag_partition=dutch_flag_partition_On_v2

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
