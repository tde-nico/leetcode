class Solution:
	def isPalindrome(self, x: int) -> bool:
		string = str(x)
		e = len(string) - 1
		s = 0
		while s < e:
			if string[s] != string[e]:
				return False
			s += 1
			e -= 1
		return True
