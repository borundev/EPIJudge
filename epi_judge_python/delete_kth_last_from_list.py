from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    dummy_head=ListNode(0,L)

    p_fast=L

    # p_slow will point at the node prior to the one to delete
    p_slow=dummy_head

    # we advance the fast pointer k steps
    for _ in range(k):
        p_fast=p_fast.next

    # if it is already at None we remove the first element (eg L=[2,1] and k=2)
    # otherwise we advance both till p_fast does not reach the tail

    while p_fast:
        p_slow=p_slow.next
        p_fast=p_fast.next

    p_slow.next=p_slow.next.next

    return dummy_head.next



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
