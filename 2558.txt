class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g = [-x for x in gifts]
        heapq.heapify(g)
        x, i = 1 << 32, 0
        while i < k and x > 1:
            x = -heapq.heappop(g)
            heapq.heappush(g, -isqrt(x))
            i += 1
        return -sum(g)
        