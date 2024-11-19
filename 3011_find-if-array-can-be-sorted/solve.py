class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pmax = 0
        cmax = nums[0]
        pcnt = cmax.bit_count()
        for v in nums:
            ccnt = v.bit_count()
            if pcnt == ccnt:
                cmax = max(cmax, v)
            else:
                pmax = cmax
                cmax = v
                pcnt = ccnt
            if v < pmax:
                return False
        return v >= pmax
