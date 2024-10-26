from typing import Counter

class Solution:
	def firstUniqChar(self, s: str) -> int:
		c = Counter(s)
		for i, v in enumerate(s):
			if c[v] == 1:
				return i
		return -1

