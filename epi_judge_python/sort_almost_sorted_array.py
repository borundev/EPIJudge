from typing import Iterator, List

from test_framework import generic_test
import itertools
import heapq

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:

    result = []

    min_heap = []

    # note the use of itertools.islice to extract slice from an iterator
    for x in itertools.islice(sequence,k):
        heapq.heappush(min_heap,x)

    while min_heap:
        x=next(sequence,None)
        if x is not None:
            val = heapq.heappushpop(min_heap,x)
        else:
            val = heapq.heappop(min_heap)
        result.append(val)


    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
