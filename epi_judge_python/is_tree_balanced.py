from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

class HeightAndStatus:
    def __init__(self,height,balanced):
        self.height=height
        self.balanced=balanced

    def __bool__(self):
        return self.balanced

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:




    def helper(root):
        """
        This function returns the height of the tree and raises an excpetion if it is unbalanced
        :param root:
        :return:
        """
        if not root:
            return HeightAndStatus(-1,True)
        else:
            left=helper(root.left)
            if not left:
                return left

            right=helper(root.right)
            if not right:
                return right

            balanced = abs(left.height-right.height)<=1
            height = max(left.height,right.height)+1
            return HeightAndStatus(height,balanced)
    result=helper(tree)
    return result.balanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
