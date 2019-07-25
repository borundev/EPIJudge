from test_framework import generic_test

def multiply(num1, num2):
    sgns=list(map(lambda x: -1 if x[0]<1 else 1,(num1,num2)))
    sgn=sgns[0]*sgns[1]
    num1[0]*=sgns[0]
    num2[0]*=sgns[1]

    # array with sufficient indices to store result
    result=[0]*(len(num1)+len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):

            # this needs a bit thinking but take m digit and n digit numbers then the last element
            # of the result is obtained from i=n-1 and j=m-1 and its location is n+m-1 which is
            # i+j+1

            result[i+j+1]+=num1[i]*num2[j]

            # this result for location i+j+1 should be adjusted to put the carry on the _next_ one which in this
            # way of writing is i+j and it itself should contain the mod

            result[i+j]+=result[i+j+1]//10
            result[i + j + 1] %=10

    # we knock off leading 0s

    while result and not result[0]:
        # should probably use deque but didn't make difference when tested
        result.pop(0)

    # finally we replace the total sign on the most significant digit
    try:
        result[0]*=sgn
    except IndexError:
        # if there is an index error it means that result is [] after removing leading 0s
        return [0]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
