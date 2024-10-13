class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	def __repr__(self):
		return f'{self.val} -> {self.next}'

from solve import Solution

def build_list(arr):
	l1 = ListNode()
	tmp = l1
	for i in arr:
		tmp.next = ListNode(i)
		tmp = tmp.next
	return l1.next

def test(case, expected):
	s = Solution()
	lists = list(map(build_list, case))
	output = s.mergeKLists(lists)
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
		'case': [[1,4,5],[1,3,4],[2,6]],
		'expected': [1,1,2,3,4,4,5,6],
	},
	{
		'case': [],
		'expected': [],
	},
	{
		'case': [[]],
		'expected': [],
	},
]

if __name__ == '__main__':
	main()
