from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.minEnd(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [3, 4],
		'expected': 6,
	},
	{
		'case': [2, 7],
		'expected': 15,
	},
]

if __name__ == '__main__':
	main()
