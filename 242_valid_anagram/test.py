from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.groupAnagrams(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': ["eat","tea","tan","ate","nat","bat"],
		'expected': [["eat","tea","ate"],["tan","nat"],["bat"]],
	},
	{
		'case': [""],
		'expected': [[""]],
	},
	{
		'case': ["a"],
		'expected': [["a"]],
	},
]

if __name__ == '__main__':
	main()
