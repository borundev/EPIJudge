import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:

    """
    We maintain a sliding window with the right edge expanding till all words in keywords are
    covered and then the left sliding till the condition is just not met by the previous slide

    :param paragraph:
    :param keywords:
    :return:
    """

    # the running_counter maintains count of words in running window
    running_counter=collections.Counter()

    # this maintains how many unique words are missing in the window
    remaining_to_cover = len(keywords)

    start = 0
    min_distance = float('inf')
    s=Subarray(-1,-1)

    for end,word in enumerate(paragraph):
        if word in keywords:
            if running_counter.get(word,0)==0:
                # if a new word is seen in the window reduce remaining_to_cover
                remaining_to_cover -= 1
            running_counter[word]+=1


        while remaining_to_cover==0:
            if end-start < min_distance:
                min_distance = end-start
                s=Subarray(start,end)
            word_start = paragraph[start]
            if word_start in keywords:
                running_counter[word_start]-=1

                # if running counter goes to zero so the word is missing in the window then
                # increase remaining_to_cover
                if running_counter.get(word_start,0)==0:
                    remaining_to_cover+=1

            start+=1

    return s


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
