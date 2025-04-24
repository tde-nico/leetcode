class Solution:
	def minAddToMakeValid(self, s: str) -> int:
		c1 = 0
		c2 = 0
		for p in s:
			if p == '(':
				c1 += 1
			else:
				if c1 > 0:
					c1 -= 1
				else:
					c2 += 1 
		return c1 + c2
