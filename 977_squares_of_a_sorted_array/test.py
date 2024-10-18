from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.sortedSquares(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')

def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [-4,-1,0,3,10],
		'expected': [0,1,9,16,100],
	},
	{
		'case': [-7,-3,2,3,11],
		'expected': [4,9,9,49,121],
	},
]

if __name__ == '__main__':
	main()
