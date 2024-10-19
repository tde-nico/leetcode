from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.runningSum(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': [1,2,3,4],
		'expected': [1,3,6,10],
	},
	{
		'case': [1,1,1,1,1],
		'expected': [1,2,3,4,5],
	},
	{
		'case': [3,1,2,10,1],
		'expected': [3,4,6,16,17],
	},
]

if __name__ == '__main__':
	main()
