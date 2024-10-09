from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.containsDuplicate(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': [1,2,3,1],
		'expected': True,
	},
	{
		'case': [1,2,3,4],
		'expected': False,
	},
	{
		'case': [1,1,1,3,3,4,3,2,4,2],
		'expected': True,
	},
]

if __name__ == '__main__':
	main()
