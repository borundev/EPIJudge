from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    MAPPINGS=('0','1',
              'ABC',
              'DEF',
              'GHI',
              'JKL',
              'MNO',
              'PQRS',
              'TUV',
              'WXYZ')



    def mnemonic_helper(d):
        if d==len(phone_number):
            result.append(''.join(partial_result))
        else:
            n=int(phone_number[d])
            for c in MAPPINGS[n]:
                partial_result.append(c)
                mnemonic_helper(d+1)
                partial_result.pop()


    result = []
    partial_result=[]
    mnemonic_helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
