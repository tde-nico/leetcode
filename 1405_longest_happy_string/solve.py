import heapq

class Solution:
	def longestDiverseString(self, a: int, b: int, c: int) -> str:
		pq = []
		if a > 0:
			heapq.heappush(pq, (-a, 'a'))
		if b > 0:
			heapq.heappush(pq, (-b, 'b'))
		if c > 0:
			heapq.heappush(pq, (-c, 'c'))
		
		res = []
		while pq:
			count1, c1 = heapq.heappop(pq)
			if len(res) >= 2 and res[-1] == c1 and res[-2] == c1:
				if not pq:
					break
				count2, c2 = heapq.heappop(pq)
				res.append(c2)
				count2 += 1
				if count2 < 0:
					heapq.heappush(pq, (count2, c2))
				heapq.heappush(pq, (count1, c1))
			else:
				res.append(c1)
				count1 += 1
				if count1 < 0:
					heapq.heappush(pq, (count1, c1))
		return ''.join(res)
