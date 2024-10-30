from heapq import heappush, heappop

class Solution:
	def minGroups(self, intervals: List[List[int]]) -> int:
		intervals.sort()
		pq = []
		for s, e in intervals:
			if pq and pq[0] < s:
				heappop(pq)
			heappush(pq, e)
		return len(pq)
