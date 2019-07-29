import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0, l1):
    # TODO - you fill in here.

    # c0 is length of l0
    head, c0 = l0, 0
    while head:
        head = head.next
        c0 += 1

    # c1 is length of l1
    head, c1 = l1, 0
    while head:
        head = head.next
        c1 += 1

    # d is difference in length and we call the longer one l0
    d = c0 - c1

    if d < 0:
        d, l0, l1 = -d, l1, l0

    # advance l0 by d steps
    for _ in range(d):
        l0 = l0.next

    # now l0 and l1 are equal length. If they now point to the same after comoving then they overlap
    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next



    return l0


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
