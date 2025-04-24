class Solution:
	def isPalindrome(self, string: str) -> bool:
		e = len(string) - 1
		s = 0
		while s < e:
			if not string[s].isalnum():
				s += 1
				continue
			if not string[e].isalnum():
				e -= 1
				continue
			if string[s].lower() != string[e].lower():
				return False
			s += 1
			e -= 1
		return True
