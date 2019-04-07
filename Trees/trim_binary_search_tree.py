"""
Problem:
Given the root of a binary search tree (BST) and 2 numbers min and max, trim the tree
such that all the numbers in the new tree are between min and max (inclusive).
The resulting tree should still be a valid binary search tree.

Ref:
https://en.wikipedia.org/wiki/Binary_search_tree
https://www.geeksforgeeks.org/binary-search-tree-data-structure/

Binary Search Tree is a node-based binary tree data structure which has the following properties:
    - The left subtree of a node contains only nodes with keys lesser than the node’s key.
    - The right subtree of a node contains only nodes with keys greater than the node’s key.
    - The left and right subtree each must also be a binary search tree.
"""


def trim_BST(tree, min_val, max_val):

    if not tree:
        return

    if min_val <= tree.val <= max_val:
        return tree

    if tree.val < min_val:
        return trim_BST(tree.right, min_val, max_val)  # Recursive call

    if tree.val > max_val:
        return trim_BST(tree.left, min_val, max_val)  # Recursive call
