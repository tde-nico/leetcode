from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.findKthBit(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [3, 1],
		'expected': '0',
	},
	{
		'case': [4, 11],
		'expected': '1',
	},
]

if __name__ == '__main__':
	main()
