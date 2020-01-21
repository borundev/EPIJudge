from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    BalancedStatusWithHeight=collections.namedtuple('BalancedStatusWithHeight',
                                                    ('balanced','height'))

    def check_balanced_tree(tree):
        if not tree:
            return BalancedStatusWithHeight(True,-1)

        lr=check_balanced_tree(tree.left)
        if not lr.balanced:
            return lr

        rr=check_balanced_tree(tree.right)
        if not rr.balanced:
            return rr

        return BalancedStatusWithHeight(abs(lr.height-rr.height)<=1,max(lr.height,rr.height)+1)

    return check_balanced_tree(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced_DONE.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
