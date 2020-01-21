from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:

    def __init__(self):
        # A list of tuples with (val,max_at_insert)
        # max_at_insert is the max when the value is inserted
        self.l=[]


    def empty(self) -> bool:
        # TODO - you fill in here.
        return not bool(len(self.l))

    def max(self) -> int:
        # TODO - you fill in here.
        try:
            return self.l[-1][1]
        except IndexError:
            return -float('inf')


    def pop(self) -> int:
        # TODO - you fill in here.
        try:
            return self.l.pop()[0]
        except IndexError:
            return

    def push(self, x: int) -> None:
        # TODO - you fill in here.
        # the max at time of insert is the max of new value and old max
        n_max=max(x,self.max())
        self.l.append((x,n_max))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
