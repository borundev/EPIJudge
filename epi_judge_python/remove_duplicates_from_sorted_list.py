from typing import Optional

from list_node import ListNode
from test_framework import generic_test

<<<<<<< HEAD:epi_judge_python/remove_duplicates_from_sorted_list_DONE.py
def remove_duplicates(L):
=======

def remove_duplicates(L: ListNode) -> Optional[ListNode]:
>>>>>>> master:epi_judge_python/remove_duplicates_from_sorted_list.py
    # TODO - you fill in here.
    it=L
    while it:
        while it.next and it.data==it.next.data:
            it.next=it.next.next
        it=it.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
<<<<<<< HEAD:epi_judge_python/remove_duplicates_from_sorted_list_DONE.py
            "remove_duplicates_from_sorted_list_DONE.py",
=======
            'remove_duplicates_from_sorted_list.py',
>>>>>>> master:epi_judge_python/remove_duplicates_from_sorted_list.py
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
