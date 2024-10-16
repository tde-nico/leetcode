from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.numJewelsInStones(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': ["aA", "aAAbbbb"],
		'expected': 3,
	},
	{
		'case': ["z", "ZZ"],
		'expected': 0,
	},
]

if __name__ == '__main__':
	main()
