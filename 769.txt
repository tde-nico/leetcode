class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        c = 0
        diff = 0
        for i, x in enumerate(arr):
            diff += x - i
            c += (diff==0)
        return c