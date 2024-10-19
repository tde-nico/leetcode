class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		res = []
		value = 0
		for n in nums:
			value += n
			res.append(value)
		return res
