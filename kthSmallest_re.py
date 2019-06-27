'''
Quest:
    Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

    Note:
    You may assume k is always valid, 1 <= k <= BST's total elements.

    Example 1:
    Input: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    Output: 1

    Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    Output: 3

    Follow up:
    What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
    How would you optimize the kthSmallest routine?

Solution:
    - it's a BST, which means left < root < right
    - use recursion to search from left to right, use self.k as a counter

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    # used for traversal k, from left - root - right
    def helper(self, node):
        if not node:
            return

        self.helper(node.left) # first left
        self.k -= 1 # then root
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right) # finally right
