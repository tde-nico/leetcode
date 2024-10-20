from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.areSentencesSimilar(*case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])


cases = [
	{
		'case': ["My name is Haley", "My Haley"],
		'expected': True,
	},
	{
		'case': ["of", "A lot of words"],
		'expected': False,
	},
	{
		'case': ["Eating right now", "Eating"],
		'expected': True,
	},
]

if __name__ == '__main__':
	main()
