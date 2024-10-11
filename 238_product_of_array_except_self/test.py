from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.productExceptSelf(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])



cases = [
	{
		'case': [1,2,3,4],
		'expected': [24,12,8,6],
	},
	{
		'case': [-1,1,0,-3,3],
		'expected': [0,0,9,0,0],
	},
]

if __name__ == '__main__':
	main()
