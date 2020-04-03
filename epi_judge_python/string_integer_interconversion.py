from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x==0:
        return '0'

    str_array=[]
    negative=''
    if x<0:
        negative='-'
        x*=-1

    while x:
        r=x%10
        x=x//10
        str_array.append(chr(ord('0')+r))

    return negative+''.join(reversed(str_array))


def string_to_int(s: str) -> int:

    if s[0]=='-':
        is_negative=-1
        s=s[1:]
    elif s[0]=='+':
        s=s[1:]
        is_negative=1
    else:
        is_negative=1

    result=0
    for c in s:
        result *=10
        result+=ord(c)-ord('0')

    return is_negative*result


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
