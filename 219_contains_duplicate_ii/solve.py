class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		d = {}
		for i, n in enumerate(nums):
			j = d.get(n, None)
			if j is None:
				d[n] = i
			else:
				if i - j <= k:
					return True
				d[n] = i
		return False
