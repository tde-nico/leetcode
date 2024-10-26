class Solution:
	def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
		if len(nums) == 0 or indexDiff < 0 or valueDiff < 0:
			return False
		bs = {}
		w = valueDiff + 1
		for i, n in enumerate(nums):
			b = n // w
			
			if b in bs:
				return True
			if b-1 in bs and n - bs[b-1] <= valueDiff:
				return True
			if b+1 in bs and bs[b+1] - n <= valueDiff:
				return True

			bs[b] = n

			if i >= indexDiff:
				del bs[nums[i - indexDiff] // w]

		return False
