'''
Quest:
    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.
    For example, given
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7

Solution:
    - preorder can tell you the root
        then inorder can tell you what's left and what's right
        so, we just need to split these lists anchored at root, then use recursion
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            # need to pop the root out, so pop(0) can always give the current root
            nodeIndex = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[nodeIndex])
            root.left = self.buildTree(preorder, inorder[0:nodeIndex])
            root.right = self.buildTree(preorder, inorder[nodeIndex+1:])

            return root