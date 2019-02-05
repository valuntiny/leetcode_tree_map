'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []  # for storing result
        temp = []  # temp for each row scanning
        flag = 1  # 1: left to right, 2: right to left
        stack = [root]  # for the leaf

        if not root: return []
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)

            res.append(temp[::flag])
            flag *= -1
            temp = []

        return res