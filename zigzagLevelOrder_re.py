'''
Quest:
    Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

    For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]

Solution:
    - recursion? no
    - iteration: need tmp to store all nodes on each level
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if not root:
            return res

        stk = [root]
        tmp = []
        flag = 1 # 1 means from left to right, -1 means from right to left
        while stk:
            for i in range(len(stk)):
                node = stk.pop(0)
                tmp.append(node.val)
                if node.left: stk.append(node.left)
                if node.right: stk.append(node.right)

            res.append(tmp[::flag])
            flag *= -1
            tmp = []

        return res