class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		return f'{self.val} -> {self.next}'

from solve import Solution

def test(case, expected):
	s = Solution()
	l1 = ListNode()
	tmp = l1
	for i in case[0]:
		tmp.next = ListNode(i)
		tmp = tmp.next
	l2 = ListNode()
	tmp = l2
	for i in case[1]:
		tmp.next = ListNode(i)
		tmp = tmp.next
	output = s.mergeTwoLists(l1.next, l2.next)
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
		'case': [[1,2,4], [1,3,4]],
		'expected': [1,1,2,3,4,4],
	},
	{
		'case': [[], []],
		'expected': [],
	},
	{
		'case': [[], [0]],
		'expected': [0],
	},
]

if __name__ == '__main__':
	main()
