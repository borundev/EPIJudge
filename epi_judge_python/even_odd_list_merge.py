from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    dummy_head_even=ListNode()
    dummy_head_odd=ListNode()
    tails,turn=[dummy_head_even,dummy_head_odd],0

    while L:
        tails[turn].next=L
        L=L.next
        tails[turn]=tails[turn].next
        turn ^= 1

    tails[1].next=None
    tails[0].next=dummy_head_odd.next
    return dummy_head_even.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
