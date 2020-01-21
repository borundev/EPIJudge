from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    l=[]
    closers={'(':')','{':'}','[':']'}
    for c in s:
        if c in closers:
            l.append(c)
        else:
            if not l or not closers[l.pop()] == c:
                return False
    return not l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
