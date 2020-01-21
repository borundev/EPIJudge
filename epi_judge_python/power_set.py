from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    n = len(input_set)

    result=[]
    for x in range(1 << n):
        m = set()
        i = 0
        while x:
            if x & 1:
                m.add(input_set[i])
            x = x >> 1
            i += 1
        result.append(list(m))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
