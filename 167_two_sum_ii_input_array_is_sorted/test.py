from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.twoSum(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[2,7,11,15], 9],
		'expected': [1,2],
	},
	{
		'case': [[2,3,4], 6],
		'expected': [1,3],
	},
	{
		'case': [[-1,0], -1],
		'expected': [1,2],
	},
]

if __name__ == '__main__':
	main()
