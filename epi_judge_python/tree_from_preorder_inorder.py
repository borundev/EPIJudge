from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    val_to_idx_for_inorder = {val:idx for idx,val in enumerate(inorder)}

    def helper(preorder_start,preorder_end,inorder_start,inorder_end):

        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return None

        val = preorder[preorder_start]
        idx_of_val_in_inorder = val_to_idx_for_inorder[val]
        left_size = idx_of_val_in_inorder - inorder_start

        node = BinaryTreeNode(val,
                              helper(preorder_start+1,
                                     preorder_start+1+left_size,
                                     inorder_start,
                                     idx_of_val_in_inorder
                                     ),
                              helper(preorder_start+1+left_size,
                                     preorder_end,
                                     idx_of_val_in_inorder+1,
                                     inorder_end
                                     )
                              )

        return node

    return helper(0,len(preorder),0,len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
