from typing import List

from test_framework import generic_test
from collections import namedtuple
import heapq

ValList=namedtuple('ValList',('value','list_idx'))

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    # Make iterators from sorted_arrays
    # This will help handle empty lists
    sorted_arrays_iter = list(map(iter,sorted_arrays))

    # build the heap
    min_heap=[]

    for i,it in enumerate(sorted_arrays_iter):
        val=next(it,None)
        if val is not None:
            heapq.heappush(min_heap,ValList(val,i))

    result=[]
    while min_heap:
        vallist = heapq.heappop(min_heap)
        result.append(vallist.value)
        newval = next(sorted_arrays_iter[vallist.list_idx], None)
        if newval is not None:
            heapq.heappush(min_heap, ValList(newval, vallist.list_idx))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
