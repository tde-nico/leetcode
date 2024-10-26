# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __repr__(self):
		return f'{self.val} -> ({self.left}, {self.right})'

class Solution:
	def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
		def dfs(r1, r2):
			if r1 is None and r2 is None:
				return True
			if (r1 is None and r2 is not None) or \
				(r1 is not None and r2 is None) or \
				(r1.val != r2.val):
				return False
			return (
				(dfs(r1.left, r2.left) or dfs(r1.left, r2.right)) and \
				(dfs(r1.right, r2.right) or dfs(r1.right, r2.left))
			)
		return dfs(root1, root2)
