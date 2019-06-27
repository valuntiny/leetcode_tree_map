'''
Quest:
    Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node,
    the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

    Note:

    You may only use constant extra space.
    Recursive approach is fine, implicit stack space does not count as extra space for this problem.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

Solution:
    - sth similar to zigzag? use stack to store the nodes in each level
'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        if not root:
            return None

        stk = [root]
        while stk:
            n = len(stk)
            for i in range(n):
                if 0 <= i < n-1:
                    stk[0].next = stk[1]
                else:
                    stk[0].next = None
                node = stk.pop(0)
                if node.left: stk.append(node.left)
                if node.right: stk.append(node.right)

        return root
