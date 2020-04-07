from test_framework import generic_test


def square_root(k: int) -> int:
    start, end = 0,k
    while start <= end:
        mid = start + (end-start)//2
        if mid**2==k:
            return mid
        elif mid**2<k:
            start=mid+1
        else:
            end=mid-1

    return start-1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
