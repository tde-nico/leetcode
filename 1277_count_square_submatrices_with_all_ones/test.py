from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.countSquares(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[0,1,1,1],[1,1,1,1],[0,1,1,1]],
		'expected': 15,
	},
	{
		'case': [[1,0,1],[1,1,0],[1,1,0]],
		'expected': 7,
	},
]

if __name__ == '__main__':
	main()
