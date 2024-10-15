import heapq

class Solution:
	def smallestRange(self, nums: List[List[int]]) -> List[int]:
		pq = []
		m = float('-inf')
		for i in range(len(nums)):
			heapq.heappush(pq, (nums[i][0], i, 0))
			m = max(m, nums[i][0])
		s = [float('-inf'), float('inf')]
		while pq:
			curr_min, list_idx, i = heapq.heappop(pq)
			if m - curr_min < s[1] - s[0]:
				s = [curr_min, m]
			if i + 1 >= len(nums[list_idx]):
				break
			nxt = nums[list_idx][i+1]
			heapq.heappush(pq, (nxt, list_idx, i+1))
			m = max(m, nxt)
		return s
