from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.myPow(*case)
	output = round(output, 10)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [2.0, 10],
		'expected': 1024.0,
	},
	{
		'case': [2.1, 3],
		'expected': 9.261,
	},
	{
		'case': [2.0, -2],
		'expected': 0.25,
	},
]

if __name__ == '__main__':
	main()
