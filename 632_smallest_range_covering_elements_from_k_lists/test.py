from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.smallestRange(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')

def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]],
		'expected': [20,24],
	},
	{
		'case': [[1,2,3],[1,2,3],[1,2,3]],
		'expected': [1,1],
	},
]

if __name__ == '__main__':
	main()
