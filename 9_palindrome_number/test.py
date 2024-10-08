from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.isPalindrome(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': 121,
		'expected': True,
	},
	{
		'case': -121,
		'expected': False,
	},
	{
		'case': 10,
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
