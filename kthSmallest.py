'''
iven a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.helper(root)

        return self.res

    def helper(self, node):
        if not node:
            return

        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)