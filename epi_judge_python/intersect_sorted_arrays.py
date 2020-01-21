from test_framework import generic_test
import bisect
import math

def intersect_two_sorted_arrays_1(A, B):


    # let lengths of A and B be m and n

    def in_B(k):
        # finds if k is in B in O(log n)
        i=bisect.bisect_left(B,k)
        return i<len(B) and B[i]==k

    res=[]
    # just the loop takes O(m) but the in_B part is O(log n)
    # so total time is O(m log n)
    for i,a in enumerate(A):
        if (not i or A[i-1]!=a) and in_B(a):
            res.append(a)

    return res


def intersect_two_sorted_arrays_2(A, B):

    i,j=0,0
    res=[]

    while i<len(A) and j<len(B):
        if A[i]==B[j]:
            if i==0 or A[i-1] != A[i]:
                res.append(A[i])
            i,j=i+1,j+1
        elif A[i]<B[j]:
            i+=1
        else:
            j+=1

    return res

def intersect_two_sorted_arrays(A, B):

    if len(A)<len(B):
        A,B=B,A

    if not A or not B:
        return intersect_two_sorted_arrays_1(A, B)

    m,n=len(A),len(B)
    if m<n/(math.log(n)-1):
        return intersect_two_sorted_arrays_1(A,B)
    else:
        return intersect_two_sorted_arrays_2(A, B)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays_DONE.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
