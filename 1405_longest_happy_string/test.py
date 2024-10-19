from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.longestDiverseString(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')

def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [1, 1, 7],
		'expected': "ccaccbcc",
	},
	{
		'case': [7, 1, 0],
		'expected': "aabaa",
	},
]

if __name__ == '__main__':
	main()
