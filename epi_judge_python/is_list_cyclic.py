import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle(head: ListNode) -> Optional[ListNode]:
    '''
    Takes a node on the loop and the head and returns the node
    that is in front of the head by the length of the loop number of
    steps
    :param on_loop:
    :param head:
    :return:
    '''
    start=on_loop
    adv_it=head
    while True:
        start=start.next
        adv_it=adv_it.next
        if start is on_loop:
            return adv_it

def has_cycle(head):
    slow,fast=head,head
    while fast and fast.next and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow is fast:
            # A loop has been found

            # Two pointers that are separated by the length of the loop
            # The lagging one starts at the head
            lag_it,adv_it=head,advance_iterator(slow,head)


            while lag_it is not adv_it:
                lag_it=lag_it.next
                adv_it=adv_it.next

            return lag_it



@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
