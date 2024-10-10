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
		'case': "A man, a plan, a canal: Panama",
		'expected': True,
	},
	{
		'case': "race a car",
		'expected': False,
	},
	{
		'case': " ",
		'expected': True,
	},
]

if __name__ == '__main__':
	main()
