from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    # dummy head will point at the head of the list
    # sublist head will point at the first element of the sublist (which will change)
    dummy_head = sublist_head = ListNode(0,L)

    # recall that first element of the list is called 1 here
    for _ in range(1,start):
        sublist_head = sublist_head.next

    # we point at the first member of the sublist and keep moving the node next to it
    # to the beginning of the sublist

    # the variable first_element_sublist will start of pointing to the first element of the
    # sublist and will keep pointing to the same node but
    # it will end up pointing to the last element of the sublist

    first_element_sublist = sublist_head.next

    for _ in range(finish-start):
        tmp=first_element_sublist.next
        sublist_head.next, tmp.next, first_element_sublist.next  \
            = tmp, sublist_head.next, tmp.next

    return dummy_head.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
