from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.firstUniqChar(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "leetcode",
		'expected': 0,
	},
	{
		'case': "loveleetcode",
		'expected': 2,
	},
	{
		'case': "aabb",
		'expected': -1,
	},
]

if __name__ == '__main__':
	main()
