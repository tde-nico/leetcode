class Solution:
	def isValid(self, s: str) -> bool:
		p = []
		for c in s:
			if c in '([{':
				p.append(c)
			else:
				if not p or \
					(c == ')' and p[-1] != '(') or \
					(c == ']' and p[-1] != '[') or \
					(c == '}' and p[-1] != '{'):
					return False
				p.pop()
		return not p
