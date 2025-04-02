class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = Counter()
        for r in matrix:
            pattern = tuple(r) if r[0] == 0 else tuple(bit ^ 1 for bit in r)
            freq[pattern] += 1   
        return max(freq.values())