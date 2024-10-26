class Solution:
	def maximumSwap(self, num: int) -> int:
		s = list(str(num))
		last = {int(d): i for i, d in enumerate(s)}
		for i, digit in enumerate(s):
			for d in range(9, int(digit), -1):
				if last.get(d, -1) > i:
					s[i], s[last[d]] = s[last[d]], s[i]
					return int(''.join(s))
		return num
