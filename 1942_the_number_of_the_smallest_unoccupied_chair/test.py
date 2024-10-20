from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.smallestChair(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[[1,4],[2,3],[4,6]], 1],
		'expected': 1,
	},
	{
		'case': [[[3,10],[1,5],[2,6]], 0],
		'expected': 2,
	},
]

if __name__ == '__main__':
	main()
