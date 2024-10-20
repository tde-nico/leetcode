from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minSwaps(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': "][][",
		'expected': 1,
	},
	{
		'case': "]]][[[",
		'expected': 2,
	},
	{
		'case': "[]",
		'expected': 0,
	},
]

if __name__ == '__main__':
	main()
