from typing import List

from test_framework import generic_test, test_utils
import math

def generate_power_set(input_set: List[int]) -> List[List[int]]:
    """The elements of the power set are mapped to all integers from 0 to 2^n-1. The elements of
    each set are the elements of the original set that are at locations of the bits that are set to
    one for the aforementiond integers.

    Thus fir each integer we go over the bits to see which ones are one. The first such element is
    given by x & ~(x-1) and we then set it to zero by x &= (x-1). Thus we do not loop over all the
    bits but only over the ones that are set to 1.
    """
    n = len(input_set)

    result=[]
    for x in range(1 << n):
        m = []

        while x:
            m.append(input_set[int(math.log2(x & ~(x-1)))])
            x &= (x-1)
        result.append(list(m))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
