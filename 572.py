# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        if r1 is None or r2 is None:
            return False
        if r1.val != r2.val:
            return False
        return self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        