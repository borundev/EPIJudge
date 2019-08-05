from test_framework import generic_test


class Queue:

    def __init__(self):
        self.l1=[]
        self.l2=[]

    def enqueue(self, x):
        self.l1.append(x)
        return

    def dequeue(self):
        if self.l2:
            return self.l2.pop()
        else:
            while len(self.l1)>1:
                self.l2.append(self.l1.pop)
            return self.l1.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks_DONE.py",
                                       'queue_from_stacks.tsv', queue_tester))
