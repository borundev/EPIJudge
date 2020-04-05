from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import namedtuple
TreeFirstVisit=namedtuple('TreeFirstVisit',('tree','firstvisit'))

def postorder_traversal(tree: BinaryTreeNode) -> List[int]:

    result = []
    stack = [TreeFirstVisit(tree,True)]

    while stack:
        stack_element = stack.pop()
        if stack_element.tree:
            if not stack_element.firstvisit:
                result.append(stack_element.tree.data)
            else:
                stack.append(TreeFirstVisit(stack_element.tree,False))
                stack.append(TreeFirstVisit(stack_element.tree.right, True))
                stack.append(TreeFirstVisit(stack_element.tree.left, True))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_postorder.py',
                                       'tree_postorder.tsv',
                                       postorder_traversal))
