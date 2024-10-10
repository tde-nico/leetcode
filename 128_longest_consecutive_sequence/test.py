from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.longestConsecutive(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [100,4,200,1,3,2],
		'expected': 4,
	},
	{
		'case': [0,3,7,2,5,8,4,6,0,1],
		'expected': 9,
	},
]

if __name__ == '__main__':
	main()
