class Node:
	def __init__(self, val, index):
		self.val = val
		self.index = index
		self.left = None
		self.right = None
		self.rep = []
		
	def add(self, val, index):
		if val > self.val:
			if self.right is None:
				self.right = Node(val, index)
			else:
				self.right.add(val, index)
		elif val < self.val:
			if self.left is None:
				self.left = Node(val, index)
			else:
				self.left.add(val, index)
		else:
			self.rep.append(index)
		
	def max(self):
		if self.right is None:
			r = 0
		else:
			r = self.right.max()
		if self.left is None:
			l = 0
		else:
			l = self.left.max()
		mrep = max(self.rep) if self.rep else 0
		return max(self.index, r, l, mrep)

	def max_right(self):
		mrep = max(self.rep) if self.rep else 0
		if self.right is None:
			return max(self.index, mrep)
		return max(self.index, mrep, self.right.max())
		
	def min_self(self):
		mrep = max(self.rep) if self.rep else 10**5
		return min(self.index, mrep)

class Solution:
	def maxWidthRamp(self, nums) -> int:
		tree = Node(nums[0], 0)
		for i in range(1,len(nums)):
			tree.add(nums[i], i)
		m = 0
		curr = tree
		while curr:
			tmp = curr.max_right() - curr.min_self()
			if tmp > m:
				m = tmp
			curr = curr.left
		
		return m
		
		#s = 0
		#e = len(nums) - 1
		#while nums[s] > nums[e] and s < e:
		'''
				 0
				15
			   2 6
			  34 8
			  79
		'''
		'''
			 0 1 2 3 4 5
			[6,0,8,2,1,5]
		
				 0
				1  2
				 3
				4 5
			
		'''
			# {9:5, 8:1, 1:2, 0:3, 4:6}
			#map  0 1 2 3 4 5 6 7 8 9
			#	[9,8,1,0,1,9,4,0,4,1]
			#	 .                 .
			
		#return e - s
