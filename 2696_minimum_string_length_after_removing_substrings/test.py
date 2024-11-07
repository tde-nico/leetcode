from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minLength(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "ABFCACDB",
		'expected': 2,
	},
	{
		'case': "ACBBD",
		'expected': 5,
	},
]

if __name__ == '__main__':
	main()
