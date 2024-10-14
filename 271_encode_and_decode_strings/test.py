from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.encode(case)
	output = s.decode(output)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': ["neet","code","love","you"],
		'expected': ["neet","code","love","you"],
	},
	{
		'case': ["we","say",":","yes"],
		'expected': ["we","say",":","yes"],
	},
	{
		'case': [],
		'expected': [],
	},
	{
		'case': [""],
		'expected': [""],
	},
]

if __name__ == '__main__':
	main()
