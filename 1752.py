class Solution:
    def check(self, nums: List[int]) -> bool:
        return (cnt:=sum(y<x for x, y in pairwise(nums)))==0 or (cnt==1 and nums[-1]<=nums[0])
