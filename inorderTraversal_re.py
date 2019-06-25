'''
Quest:
    Given a binary tree, return the inorder traversal of its nodes' values.

    Example:
    Input: [1,null,2,3]
       1
        \
         2
        /
       3

    Output: [1,3,2]
    Follow up: Recursive solution is trivial, could you do it iteratively?

Solution:
    - recursion is easy
    - iteration needs stack
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursion

class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

# iteration

class Solution:
    def inorderTraversal(self, root):
        res = []
        if not root:
            return res

        stk = []
        while True:
            while root:
                stk.append(root)
                root = root.left
            if not stk:
                return res
            node = stk.pop()
            res.append(node.val)
            root = node.right