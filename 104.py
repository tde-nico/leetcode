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
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		q = collections.deque([root])
		level = 0
		if root is None:
			return 0
		while q:
			for i in range(len(q)):
				curr = q.popleft()
				if curr.right:
					q.append(curr.right)
				if curr.left:
					q.append(curr.left)
			level += 1
		return level
