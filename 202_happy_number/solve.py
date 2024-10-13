class Solution:
	def isHappy(self, n: int) -> bool:
		while n > 6:
			a = n
			s = 0
			while a:
				s += (a%10) * (a%10)
				a //= 10
			n = s
		if n == 1:
			return True
		return False
