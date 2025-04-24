class Solution:
	def fizzBuzz(self, n: int) -> List[str]:
		res = []
		i = 1
		while i <= n:
			if not i % 15:
				res.append("FizzBuzz")
			elif not i % 3:
				res.append("Fizz")
			elif not i % 5:
				res.append("Buzz")
			else:
				res.append(str(i))
			i += 1
		return res
