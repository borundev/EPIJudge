from test_framework import generic_test


def evaluate(expression: str) -> int:

    result = []
    delimiter = ','

    operators = {
        '+' : lambda y,x: x+y,
        '-' : lambda y,x:x-y,
        '/' : lambda y,x:x//y,
        '*' : lambda y,x: x*y
        }

    for token in expression.split(delimiter):
        operator = operators.get(token,None)
        if not operator:
            result.append(int(token))
        else:
            y,x=result.pop(),result.pop()
            result.append(operator(y,x))
    return result.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
