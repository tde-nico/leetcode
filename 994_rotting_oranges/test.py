from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.orangesRotting(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[2,1,1],[1,1,0],[0,1,1]],
		'expected': 4,
	},
	{
		'case': [[2,1,1],[0,1,1],[1,0,1]],
		'expected': -1,
	},
	{
		'case': [[0,2]],
		'expected': 0,
	},
]

if __name__ == '__main__':
	main()
