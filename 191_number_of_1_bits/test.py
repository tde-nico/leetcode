from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.hammingWeight(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': 11,
		'expected': 3,
	},
	{
		'case': 128,
		'expected': 1,
	},
	{
		'case': 2147483645,
		'expected': 30,
	},
]

if __name__ == '__main__':
	main()
