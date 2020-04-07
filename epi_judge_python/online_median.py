from typing import Iterator, List

from test_framework import generic_test
import heapq

def online_median(sequence: Iterator[int]) -> List[float]:

    # The heap maintaing the lower half
    s_max_heap=[]

    # The heap maintaining the upper half
    l_min_heap=[]

    result=[]

    for v in sequence:
        # Push the element in the upper half
        heapq.heappush(l_min_heap,v)

        # Take out the smallest element from the upper half and push it into the lower half
        v=heapq.heappop(l_min_heap)
        heapq.heappush(s_max_heap,-v)

        # If this causes the lower half to increase in size above the upper half adjust for that
        if len(s_max_heap)>len(l_min_heap):
            v=-heapq.heappop(s_max_heap)
            heapq.heappush(l_min_heap,v)

        if len(s_max_heap)==len(l_min_heap):
            result.append((-s_max_heap[0]+l_min_heap[0])/2)
        else:
            result.append(l_min_heap[0])


    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
