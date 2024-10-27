from solve import Solution


def test(case, expected):
	s = Solution()
	output = s.parseBoolExpr(case)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')

def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': "&(|(f))",
		'expected': False,
	},
	{
		'case': "|(f,f,f,t)",
		'expected': True,
	},
	{
		'case': "!(&(f,t))",
		'expected': True,
	},
]

if __name__ == '__main__':
	main()
