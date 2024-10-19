from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.maximumWealth(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': [[1,2,3],[3,2,1]],
		'expected': 6,
	},
	{
		'case': [[1,5],[7,3],[3,5]],
		'expected': 10,
	},
	{
		'case': [[2,8,7],[7,1,3],[1,9,5]],
		'expected': 17,
	},
]

if __name__ == '__main__':
	main()
