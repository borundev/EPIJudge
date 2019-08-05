from test_framework import generic_test

def remove_duplicates(L):
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
            "remove_duplicates_from_sorted_list_DONE.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
