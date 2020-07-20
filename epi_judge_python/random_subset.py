import functools
from typing import List
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

def random_subset_v1(n,k):
    data=list(range(n))

    for i in range(k):
        random_idx= random.randint(i,n-1)
        data[i],data[random_idx] = data[random_idx],data[i]

    return data[:k]

def random_subset(n: int, k: int) -> List[int]:
    changed_elements = dict()
    for i in range(k):
        random_idx=random.randint(i,n-1)

        random_idx_mapped = changed_elements.get(random_idx,random_idx)
        i_mapped = changed_elements.get(i,i)

        changed_elements[i]=random_idx_mapped
        changed_elements[random_idx]=i_mapped

    return [changed_elements[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0) for result in results],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_subset.py', 'random_subset.tsv',
                                       random_subset_wrapper))
