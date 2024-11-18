from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.compressedString(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "abcde",
		'expected': "1a1b1c1d1e",
	},
	{
		'case': "aaaaaaaaaaaaaabb",
		'expected': "9a5a2b",
	},
]

if __name__ == '__main__':
	main()
