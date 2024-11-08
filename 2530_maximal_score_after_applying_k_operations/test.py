from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.maxKelements(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[10,10,10,10,10], 5],
		'expected': 50,
	},
	{
		'case': [[1,10,3,3,3], 3],
		'expected': 17,
	},
]

if __name__ == '__main__':
	main()
