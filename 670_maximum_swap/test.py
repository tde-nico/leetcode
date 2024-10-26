from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.maximumSwap(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': 2736,
		'expected': 7236,
	},
	{
		'case': 9973,
		'expected': 9973,
	},
]

if __name__ == '__main__':
	main()
