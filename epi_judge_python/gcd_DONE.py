from test_framework import generic_test


def gcd(x, y):
    # TODO - you fill in here.
    return x if y==0 else gcd(y,x%y)
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd_DONE.py", 'gcd.tsv', gcd))
