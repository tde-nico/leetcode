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
	output = s.addTwoNumbers(l1.next, l2.next)
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
		'case': [[2,4,3], [5,6,4]],
		'expected': [7,0,8],
	},
	{
		'case': [[0], [0]],
		'expected': [0],
	},
	{
		'case': [[9,9,9,9,9,9,9], [9,9,9,9]],
		'expected': [8,9,9,9,0,0,0,1],
	},
]

if __name__ == '__main__':
	main()
