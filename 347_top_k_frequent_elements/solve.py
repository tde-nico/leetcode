class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		l = len(nums)
		count = {}
		freq = [[] for _ in range(l+1)]
		for n in nums:
			count[n] = count.get(n, 0) + 1
		for n, c in count.items():
			freq[c].append(n)
		res = []
		r = 0
		for i in range(l, 0, -1):
			for n in freq[i]:
				res.append(n)
				r += 1
				if r == k:
					return res
