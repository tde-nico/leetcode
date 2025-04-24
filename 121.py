class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		m = 0
		b = prices[0]
		for p in prices:
			if b > p:
				b = p
			m = max(m, p - b)
		return m
