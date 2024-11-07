from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minimumSteps(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "101",
		'expected': 1,
	},
	{
		'case': "100",
		'expected': 2,
	},
	{
		'case': "0111",
		'expected': 0,
	},
]

if __name__ == '__main__':
	main()
