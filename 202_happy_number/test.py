from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.isHappy(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': 19,
		'expected': True,
	},
	{
		'case': 2,
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
