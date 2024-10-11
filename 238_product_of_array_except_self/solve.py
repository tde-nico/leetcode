class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		l = len(nums)
		res = [1] * l
		n = 1
		for i in range(l):
			res[i] *= n
			n *= nums[i]
		n = 1
		for i in range(l-1, -1, -1):
			res[i] *= n
			n *= nums[i]
		return res
