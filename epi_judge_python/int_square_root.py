from test_framework import generic_test


def square_root(k):
    left,right=0,k
    while left<=right:
        mid=(left+right)//2
        if mid**2<=k: # this <= means that the value returned below is left-1
            left=mid+1
        else:
            right=mid-1
    return left-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
