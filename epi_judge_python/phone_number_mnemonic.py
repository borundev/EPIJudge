from typing import List

from test_framework import generic_test, test_utils

MAPPINGS = ('0', '1',
            'ABC',
            'DEF',
            'GHI',
            'JKL',
            'MNO',
            'PQRS',
            'TUV',
            'WXYZ')

def phone_mnemonic(phone_number: str) -> List[str]:

    def helper(pos):
        if pos==len(phone_number):
            results.append(''.join(partial_result))
            return

        for c in MAPPINGS[int(phone_number[pos])]:
            partial_result.append(c)
            helper(pos+1)
            partial_result.pop()

    results=[]
    partial_result=[]
    helper(0)

    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
