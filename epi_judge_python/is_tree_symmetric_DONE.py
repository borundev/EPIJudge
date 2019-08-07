from test_framework import generic_test


def is_symmetric(tree):
    # TODO - you fill in here.

    def is_symmetric_inner(tree0,tree1):
        if not tree0 and not tree1:
            return True
        elif tree0 and tree1:
            return tree0.data==tree1.data and \
                   is_symmetric_inner(tree0.left,tree1.right) and \
                   is_symmetric_inner(tree0.right,tree1.left)
        else:
            return False
    return is_symmetric_inner(tree,tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric_DONE.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
