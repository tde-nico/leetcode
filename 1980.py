class Solution:
    def findDifferentBinaryString(self, nums):
        n = len(nums)
        ans = "0" * n
        
        if ans not in nums:
            return ans
        
        ans = list(ans)
        for i in range(n):
            ans[i] = '1'
            if "".join(ans) not in nums:
                return "".join(ans)
            ans[i] = '0'
        
        return "".join(ans)