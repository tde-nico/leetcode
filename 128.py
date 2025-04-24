class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		ns = set(nums)
		l = 0
		for n in ns:
			if n-1 not in ns:
				seq = n + 1
				while seq in ns:
					seq += 1
				l = max(l, seq - n)
		return l
