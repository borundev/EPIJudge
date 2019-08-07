from test_framework import generic_test


def find_nearest_repetition(paragraph):
    d={}
    m=float('inf')

    for i,word in enumerate(paragraph):
        if word in d:
            m=min(m,i-d[word])
        d[word]=i

    if m !=float('inf'):
        return int(m)
    else:
        return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries_DONE.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
