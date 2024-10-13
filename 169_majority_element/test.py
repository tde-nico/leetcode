from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.majorityElement(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [3,2,3],
		'expected': 3,
	},
	{
		'case': [2,2,1,1,1,2,2],
		'expected': 2,
	},
]

if __name__ == '__main__':
	main()
