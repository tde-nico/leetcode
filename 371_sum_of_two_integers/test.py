from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.getSum(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [1, 2],
		'expected': 3,
	},
	{
		'case': [2, 3],
		'expected': 5,
	},
]

if __name__ == '__main__':
	main()
