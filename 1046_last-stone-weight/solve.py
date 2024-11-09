import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            if first < second:
                heapq.heappush(pq, first - second)
        if not pq:
            return 0
        return abs(pq[0])
