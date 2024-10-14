from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.topKFrequent(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': [[1,1,1,2,2,3], 2],
		'expected': [1,2],
	},
	{
		'case': [[1], 1],
		'expected': [1],
	},
]

if __name__ == '__main__':
	main()
