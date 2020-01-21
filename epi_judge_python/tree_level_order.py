from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result=[]
    if not tree:
        return result
    current_layer=[tree]

    while current_layer:
        result.append([curr.data for curr in current_layer])
        current_layer=[
            child for curr in current_layer
            for child in (curr.left,curr.right) if child
        ]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
