from test_framework import generic_test


def stable_sort_list(L: ListNode) -> Optional[ListNode]:
    if L is None or L.next is None:
        return L


    # The following will haave the slow pointing pointing at beginning of the second half
    # this means we need a pre_slow pointer pointing at the slow so that we can set its next
    # to None to split the list

    slow,fast=L,L
    pre_slow=None
    while fast and fast.next:
        pre_slow=slow
        slow,fast=slow.next,fast.next.next

    if pre_slow is not None:
        pre_slow.next=None

    # sort the two lists
    L=stable_sort_list(L)
    slow=stable_sort_list(slow)

    # merge the two
    return merge_two_sorted_lists(L,slow)


def merge_two_sorted_lists(a,b):
    '''
    Takes two sorted list and merges them in a stable way
    :param a:
    :param b:
    :return:
    '''
    cls=type(a)
    dummy_head=cls()
    cur=dummy_head

    while a and b:
        if a.data<=b.data:
            cur.next=a
            a=a.next
        else:
            cur.next=b
            b=b.next
        cur=cur.next

    cur.next=a or b

    return dummy_head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list_DONE.py", 'sort_list.tsv',
                                       stable_sort_list))
