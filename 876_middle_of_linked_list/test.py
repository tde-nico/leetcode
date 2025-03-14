class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		return f'{self.val} -> {self.next}'

from solve import Solution

def test(case, expected):
	s = Solution()
	l = ListNode()
	tmp = l
	for i in case:
		tmp.next = ListNode(i)
		tmp = tmp.next
	output = s.middleNode(l.next)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	while output and expected:
		assert output.val == expected[0]
		output = output.next
		expected = expected[1:]
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [1,2,3,4,5],
		'expected': [3,4,5],
	},
	{
		'case': [1,2,3,4,5,6],
		'expected': [4,5,6],
	},
]

if __name__ == '__main__':
	main()
