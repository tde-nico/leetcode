from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.containsNearbyDuplicate(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')

def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[1,2,3,1], 3],
		'expected': True,
	},
	{
		'case': [[1,0,1,1], 1],
		'expected': True,
	},
	{
		'case': [[1,2,3,1,2,3], 2],
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
