'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            node = inorder.index(preorder.pop(0)) # the index of the tree root
            root = TreeNode(inorder[node])
            root.left = self.buildTree(preorder, inorder[0:node])
            root.right = self.buildTree(preorder, inorder[node+1:])

            return root