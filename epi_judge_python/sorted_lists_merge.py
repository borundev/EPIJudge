from test_framework import generic_test
from list_node import ListNode

def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    dummy_head=ListNode()
    p=dummy_head
    while (L1 and L2):
        if L1.data<L2.data:
            p.next=L1
            L1=L1.next
            p=p.next
        else:
            p.next=L2
            L2=L2.next
            p=p.next

    p.next=L1 or L2

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
