from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.singleNumber(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [2,2,1],
		'expected': 1,
	},
	{
		'case': [4,1,2,1,2],
		'expected': 4,
	},
	{
		'case': [1],
		'expected': 1,
	},
]

if __name__ == '__main__':
	main()
