from test_framework import generic_test
from test_framework.test_failure import TestFailure
from functools import reduce
import string

def int_to_string(x: int) -> str:

    if x == 0:
        return '0'


    is_neg=False
    if x<0:
        x,is_neg=-x,True


    s=[]

    while x:
        c=x % 10
        x = x // 10
        s.append('{}'.format(c))
    if is_neg:
        s.append('-')

    return ''.join(reversed(s))


def string_to_int(s: str) -> int:
    return reduce(lambda r,c: r*10+string.digits.index(c),s[s[0]=='-':],0)*(-1 if s[0]=='-' else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))

