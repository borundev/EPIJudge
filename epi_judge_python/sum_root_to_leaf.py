from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:

    def helper(tree, partial_sum=0):
        """

        Takes the partial_sum passed to it and multiplies it by 2 and add its own value before
        calling itself on the child nodes

        :param tree:
        :param partial_sum:
        :return:
        """
        if not tree:
            return 0

        partial_sum = 2*partial_sum+tree.data

        if not tree.left and not tree.right:
            return partial_sum

        return helper(tree.left,partial_sum)+helper(tree.right,partial_sum)

    return helper(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
