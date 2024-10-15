class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		r = dict()
		m = dict()
		for c in magazine:
			m[c] = m.get(c, 0) + 1
		for c in ransomNote:
			n = m.get(c, None)
			if n is None or n <= 0:
				return False
			m[c] = n - 1
		return True
