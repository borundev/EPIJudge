from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    def helper(tree,remaining_weight):
        if not tree:
            return False
        remaining_weight -= tree.data

        # The ONLY condition we can get match is if the left node ends up with remaning_weight 0
        if not tree.left and not tree.right:
            if remaining_weight==0:
                # Bypass the stack
                raise Exception()
            else:
                return False
        return helper(tree.left,remaining_weight) or helper(tree.right,remaining_weight)

    try:
        helper(tree,remaining_weight)
    except:
        return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
