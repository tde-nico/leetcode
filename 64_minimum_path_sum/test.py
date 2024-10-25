from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minPathSum(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[1,3,1],[1,5,1],[4,2,1]],
		'expected': 7,
	},
	{
		'case': [[1,2,3],[4,5,6]],
		'expected': 12,
	},
]

if __name__ == '__main__':
	main()
