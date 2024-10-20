class Solution:
	def minSwaps(self, s: str) -> int:
		n = 0
		for c in s:
			if c == '[':
				n += 1
			else:
				if n > 0:
					n -= 1
		return (n + 1) // 2
