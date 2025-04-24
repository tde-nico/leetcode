class Solution:
	def countMaxOrSubsets(self, nums: List[int]) -> int:
		m = 0
		for n in nums:
			m |= n
		bads = 0
		mask = m
		while mask:
			count = 0
			for n in nums:
				if not (n & mask):
					count += 1
			if bin(mask).count('1') % 2:
				bads += ((1 << count) - 1)
			else:
				bads -= ((1 << count) - 1)
			mask = (mask - 1) & m
		return (1 << len(nums)) - 1 - bads
