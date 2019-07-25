from test_framework import generic_test


def add_two_numbers(L1, L2):
    carry=0
    cls=type(L1)

    result=cls()
    cur_pos=result

    while L1 or L2 or carry:

        # Note that starting with cur_pos= cur_pos.next means the first entry in result is dummy
        # and we have to return result.next
        # This is a cute trick as otherwise, if we do the next two lines at the end of the loop
        # we would have to keep track of previous position and then set prev.next=None

        cur_pos.next = cls()
        cur_pos = cur_pos.next

        r=(L1.data if L1 else 0)+(L2.data if L2 else 0) + carry
        cur_pos.data=r % 10
        carry=r //10

        L1=L1.next if L1 else None
        L2=L2.next if L2 else None

    return result.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
