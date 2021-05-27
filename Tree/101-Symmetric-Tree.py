'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return False
        return self.isSym(root.left, root.right)
    
    def isSym(self, left, right):
        while left and right and left.val == right.val:
            return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
        return left == right 

                