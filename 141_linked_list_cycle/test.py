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
	tmp2 = l1
	for i in range(case[1]):
		tmp2 = tmp2.next
	if case[1] >= 0:
		tmp.next = tmp2
	output = s.hasCycle(l1.next)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[3,2,0,-4], 1],
		'expected': True,
	},
	{
		'case': [[1,2], 0],
		'expected': True,
	},
	{
		'case': [[1], -1],
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
