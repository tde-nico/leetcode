from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.maxProfit(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [7,1,5,3,6,4],
		'expected': 5,
	},
	{
		'case': [7,6,4,3,1],
		'expected': 0,
	},
]

if __name__ == '__main__':
	main()
