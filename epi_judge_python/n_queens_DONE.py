from test_framework import generic_test


def n_queens(n):
    # TODO - you fill in here.

    def helper_func(row):
        if row==n:
            result.append(col_result.copy())
        else:
            for col in range(n):
                for r,c in enumerate(col_result):
                    if abs(c-col) in (0,row-r):
                        break
                else:
                    col_result.append(col)
                    helper_func(row+1)
                    col_result.pop()

    result=[]
    col_result=[]
    helper_func(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens_DONE.py", 'n_queens.tsv', n_queens,
                                       comp))
