from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minAddToMakeValid(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "())",
		'expected': 1,
	},
	{
		'case': "(((",
		'expected': 3,
	},
	{
		'case': "()))((",
		'expected': 4,
	},
]

if __name__ == '__main__':
	main()
