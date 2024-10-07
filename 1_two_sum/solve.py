class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		m = {k: i for i, k in enumerate(nums)}
		for i, n in enumerate(nums):
			s = m.get(target-n, None)
			if s is not None and s != i:
				return [i, s]
