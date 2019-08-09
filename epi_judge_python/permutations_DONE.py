from test_framework import generic_test, test_utils


def permutations(A):
    # TODO - you fill in here.

    def permutations_helper(i):
        if i==len(A)-1:
            results.append(A.copy())
        else:
            # try every possible value for A[i] but only from the right as the ones on the left have already
            # been tried

            for j in range(i,len(A)):
                A[i],A[j]=A[j],A[i]
                permutations_helper(i+1)
                # rollback
                A[i], A[j] = A[j], A[i]
    results=[]
    permutations_helper(0)
    return results


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations_DONE.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
