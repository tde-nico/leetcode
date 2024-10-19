class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		m = 0
		for a in accounts:
			s = sum(a)
			m = max(m, s)
		return m
