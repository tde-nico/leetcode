class Solution:
	def myPow(self, x: float, n: int) -> float:
		if n < 0:
			x = 1 / x
			n = -n
		p = 1
		while n:
			if n & 1:
				p *= x
			x *= x
			n >>= 1
		return p
