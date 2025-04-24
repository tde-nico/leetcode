class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        losers = set()
        for u, v in edges:
            losers.add(v)
        if len(losers) != n-1:
            return -1
        for i in range(n):
            if i not in losers:
                return i
        