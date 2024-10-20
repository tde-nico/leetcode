from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.countMaxOrSubsets(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [3,1],
		'expected': 2,
	},
	{
		'case': [2,2,2],
		'expected': 7,
	},
	{
		'case': [3,2,1,5],
		'expected': 6,
	},
]

if __name__ == '__main__':
	main()
