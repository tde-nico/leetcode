import math
import heapq

class Solution:
	def maxKelements(self, nums: List[int], k: int) -> int:
		pq = [-n for n in nums]
		heapq.heapify(pq)
		s = 0
		for _ in range(k):
			m = -heapq.heappop(pq)
			s += m
			heapq.heappush(pq, -math.ceil(m / 3))
		return s
