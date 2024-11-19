from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minimumSubarrayLength(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])



cases = [
	{
		'case': [[1,2,3], 2],
		'expected': 1,
	},
	{
		'case': [[2,1,8], 10],
		'expected': 3,
	},
	{
		'case': [[1,2], 0],
		'expected': 1,
	},
]

if __name__ == '__main__':
	main()
