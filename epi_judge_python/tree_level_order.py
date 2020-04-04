from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

    result=[]
    if tree:
        queue = deque([tree])
        while queue:
            next_queue = deque()
            result.append([elem.data for elem in queue])
            while queue:
                element = queue.popleft()
                next_queue.extend(filter(lambda x: bool(x),[element.left,element.right]))
            queue = next_queue
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
