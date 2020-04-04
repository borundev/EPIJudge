from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:

    dummy_head=ListNode(0,L)
    previous_to_delete=dummy_head

    # make lead point to previous_to_delete + (k+1)
    lead=dummy_head.next
    for _ in range(k):
        lead=lead.next

    # move lead to point to the end
    while lead:
        previous_to_delete,lead=previous_to_delete.next,lead.next

    previous_to_delete.next=previous_to_delete.next.next
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
