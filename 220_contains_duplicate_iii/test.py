from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.containsNearbyAlmostDuplicate(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[1,2,3,1], 3, 0],
		'expected': True,
	},
	{
		'case': [[1,5,9,1,5,9], 2, 3],
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
