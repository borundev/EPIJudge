from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:

    class UnbalancedException(Exception):
        pass


    def helper(root):
        """
        This function returns the height of the tree and raises an excpetion if it is unbalanced
        :param root:
        :return:
        """
        if not root:
            return -1
        else:
            left=helper(root.left)
            right=helper(root.right)

            balanced= abs(left-right)<=1

            if not balanced:
                raise UnbalancedException()

            height = max(left,right)+1
            return height
    try:
        helper(tree)
    except UnbalancedException as e:
        return False
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
