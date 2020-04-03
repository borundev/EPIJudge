from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    if not L:
        return L

    master=current_head=ListNode(0,L)

    # go to the position right before start
    for _ in range(1,start):
        current_head=current_head.next


    # current will go over the part that is to be flipped
    # at the end it will point to the element right after the one flipped

    # new_tail will point to the first element to be flipped

    current=new_tail=current_head.next

    # prev points to the element before the current one
    # if we were flipping the entire list this would be set to None to begin with
    # right now it does not matter what we set it to because in the end it wiil be set
    # via new_tail.next to the element right after the last one being flipped
    # that is why we had to store it.
    prev=None

    # Note the non standard notation of the question - the first element is one and the finish
    # element is included in the counting of how many to flip unlike that for arrays

    for _ in range(finish-start+1):
        nxt=current.next
        current.next=prev
        prev=current
        current=nxt

    current_head.next=prev
    new_tail.next=current

    return master.next




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
