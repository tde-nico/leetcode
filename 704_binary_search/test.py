from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.search(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[5], 5],
		'expected': 0,
	},
	{
		'case': [[-1,0,3,5,9,12], 9],
		'expected': 4,
	},
	{
		'case': [[-1,0,3,5,9,12], 2],
		'expected': -1,
	},
]

if __name__ == '__main__':
	main()
