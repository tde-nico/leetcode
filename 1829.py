class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m = (1 << maximumBit) - 1
        k = 0
        ans = []
        for n in nums:
            k ^= n
            ans.append(k ^ m)
        return ans[::-1]
