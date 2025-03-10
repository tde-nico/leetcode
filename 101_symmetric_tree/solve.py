# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __repr__(self):
		return f'{self.val} -> ({self.left}, {self.right})'

class Solution:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		def dfs(r1, r2):
			if r1 is None and r2 is None:
				return True
			if r1 is None or r2 is None:
				return False
			return (
				r1.val == r2.val and \
				dfs(r1.left, r2.right) and \
				dfs(r1.right, r2.left)
			)
		if root is None:
			return True
		return dfs(root.left, root.right)
