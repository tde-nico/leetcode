class Solution:
	def compressedString(self, word: str) -> str:
		res = ''
		last = ''
		c = 0
		for i, w in enumerate(word):
			if c != 0 and (w != last or c == 9):
				res += str(c) + last
				c = 0
			last = w
			c += 1
		res += str(c) + last
		return res
