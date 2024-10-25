from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.climbStairs(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': 2,
		'expected': 2,
	},
	{
		'case': 3,
		'expected': 3,
	},
]

if __name__ == '__main__':
	main()
