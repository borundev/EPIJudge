from test_framework import generic_test


def evaluate(expression):
    # TODO - you fill in here.

    int_result=[]
    delimeter=','
    operators={'+': lambda y,x : x+y,
               '-': lambda y,x: x-y,
               '/': lambda y,x:x//y,
               '*': lambda y,x:x*y}

    for t in expression.split(delimeter):
        if t in operators:
            int_result.append(operators[t](int_result.pop(),int_result.pop()))
        else:
            # t is an int
            int_result.append(int(t))
    return int_result[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn_DONE.py", 'evaluate_rpn.tsv',
                                       evaluate))
