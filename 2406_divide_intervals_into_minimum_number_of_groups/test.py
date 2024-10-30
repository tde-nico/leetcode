from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minGroups(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[5,10],[6,8],[1,5],[2,3],[1,10]],
		'expected': 3,
	},
	{
		'case': [[1,3],[5,6],[8,10],[11,13]],
		'expected': 1,
	},
]

if __name__ == '__main__':
	main()
