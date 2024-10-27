from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.maxUniqueSplit(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "ababccc",
		'expected': 5,
	},
	{
		'case': "aba",
		'expected': 2,
	},
	{
		'case': "aa",
		'expected': 1,
	},
]

if __name__ == '__main__':
	main()
