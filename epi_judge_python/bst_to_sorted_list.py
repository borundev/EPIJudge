import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def bst_to_doubly_linked_list(tree: BstNode) -> Optional[BstNode]:
    from collections import namedtuple
    HeadAndTail=namedtuple('HeadAndTail',('head','tail'))

    def helper(tree):
        """
        takes a tree and returns the head and tail of a doubly linked list wrapped in HeadAndTail

        :param tree:
        :return:
        """
        if not tree:
            return HeadAndTail(None,None)

        left=helper(tree.left) # a head tail tuple of left branch of tree converted to dll
        right=helper(tree.right) # a head tail tuple of right branch of tree converted to dll

        # link the left dll to the tree node on the left
        if left.tail:
            left.tail.right=tree
        tree.left=left.tail

        # head is left.head if it exists otherwise tree
        head = left.head or tree

        # link the right dll to the tree node on the right
        if right.head:
            right.head.left=tree
        tree.right=right.head

        # tail is right.tail if it exists or tree
        tail = right.tail or tree

        return HeadAndTail(head,tail)

    return helper(tree).head


@enable_executor_hook
def bst_to_doubly_linked_list_wrapper(executor, tree):
    l = executor.run(functools.partial(bst_to_doubly_linked_list, tree))

    if l is not None and l.left is not None:
        raise TestFailure(
            'Function must return the head of the list. Left link must be None'
        )

    v = []
    while l:
        v.append(l.data)
        if l.right and l.right.left is not l:
            raise TestFailure('List is ill-formed')
        l = l.right

    return v


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_to_sorted_list.py',
                                       'bst_to_sorted_list.tsv',
                                       bst_to_doubly_linked_list_wrapper))
