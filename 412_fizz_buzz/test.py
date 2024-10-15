from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.fizzBuzz(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': 3,
		'expected': ["1","2","Fizz"],
	},
	{
		'case': 5,
		'expected': ["1","2","Fizz","4","Buzz"],
	},
	{
		'case': 15,
		'expected': ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"],
	},
]

if __name__ == '__main__':
	main()
