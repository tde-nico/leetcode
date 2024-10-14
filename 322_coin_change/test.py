from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.coinChange(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[1,2,5], 11],
		'expected': 3,
	},
	{
		'case': [[2], 3],
		'expected': -1,
	},
	{
		'case': [[1], 0],
		'expected': 0,
	},
]

if __name__ == '__main__':
	main()
