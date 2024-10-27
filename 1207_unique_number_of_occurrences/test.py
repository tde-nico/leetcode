from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.uniqueOccurrences(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [1,2,2,1,1,3],
		'expected': True,
	},
	{
		'case': [1,2],
		'expected': False,
	},
	{
		'case': [-3,0,1,-3,1,1,1,-3,10,0],
		'expected': True,
	},
]

if __name__ == '__main__':
	main()
