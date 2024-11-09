from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.romanToInt(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "III",
		'expected': 3,
	},
	{
		'case': "LVIII",
		'expected': 58,
	},
	{
		'case': "MCMXCIV",
		'expected': 1994,
	},
]

if __name__ == '__main__':
	main()
