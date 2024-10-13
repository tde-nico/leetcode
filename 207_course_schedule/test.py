from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.canFinish(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [2, [[1,0]]],
		'expected': True,
	},
	{
		'case': [2, [[1,0],[0,1]]],
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
