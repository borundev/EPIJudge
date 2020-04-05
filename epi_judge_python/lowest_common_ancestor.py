import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import namedtuple

Status=namedtuple('Status',('num_match','parent'))

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    def helper(tree, node0: BinaryTreeNode, node1: BinaryTreeNode) -> Status:
        """
        This function passes on any Status object it obtains recursively if
        status.num_match==2  which means a match was already found in a subtree
        and the lca is the status.parent

        If the tree is actually a leaf it returns a Status object with status.num_match=0

        Otherwise it makes a new Status object where the number of match is the sum of number of
        matches from the left and right subtree and that from the data of tree itself.

        :param tree:
        :param node0:
        :param node1:
        :return:
        """
        if not tree:
            return Status(0,tree)
        lr=helper(tree.left,node0,node1)
        if lr.num_match==2:
            return lr
        rr=helper(tree.right,node0,node1)
        if rr.num_match==2:
            return rr

        return Status(lr.num_match+rr.num_match+(node0,node1).count(tree),tree)
    return helper(tree,node0,node1).parent


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
