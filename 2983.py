class Solution:
	def minimumSteps(self, s: str) -> int:
		res, b = 0, 0
		for c in s:
			if c == '1':
				b += 1
			else:
				res += b
		return res
