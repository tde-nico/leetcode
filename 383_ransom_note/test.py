from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.canConstruct(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])



cases = [
	{
		'case': ["a", "b"],
		'expected': False,
	},
	{
		'case': ["aa", "ab"],
		'expected': False,
	},
	{
		'case': ["aa", "aab"],
		'expected': True,
	},
]

if __name__ == '__main__':
	main()
