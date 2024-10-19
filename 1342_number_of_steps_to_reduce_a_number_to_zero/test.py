from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.numberOfSteps(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': 14,
		'expected': 6,
	},
	{
		'case': 8,
		'expected': 4,
	},
	{
		'case': 123,
		'expected': 12,
	},
]

if __name__ == '__main__':
	main()
