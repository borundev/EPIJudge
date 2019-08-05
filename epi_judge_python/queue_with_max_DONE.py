from test_framework import generic_test
from test_framework.test_failure import TestFailure


class QueueWithMax:
    def __init__(self):
        self.l=[]
        self.max_and_next_max={}
        self.global_max=0

    def enqueue(self, x):
        # TODO - you fill in here.
        self.l.append(x)
        if x>self.global_max:

        return

    def dequeue(self):
        # TODO - you fill in here.
        x=self.popleft()
        return x

    def max(self):
        # TODO - you fill in here.
        return 0


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max_DONE.py",
                                       'queue_with_max.tsv', queue_tester))
