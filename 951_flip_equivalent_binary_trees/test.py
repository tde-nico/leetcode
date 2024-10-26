class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __repr__(self):
		return f'{self.val} -> ({self.left}, {self.right})'

from solve import Solution

def test(case, expected):
	s = Solution()
	def build_tree(arr, i, n):
		root = None
		if i < n and arr[i] is not None:
			root = TreeNode(arr[i])
			root.left = build_tree(arr, 2 * i + 1, n)
			root.right = build_tree(arr, 2 * i + 2, n)
		return root
	root1 = build_tree(case[0], 0, len(case[0]))
	root2 = build_tree(case[1], 0, len(case[1]))
	output = s.flipEquiv(root1, root2)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[1,2,3,4,5,6,None,None,None,7,8], [1,3,2,None,6,4,5,None,None,None,None,None,None,8,7]],
		'expected': True,
	},
	{
		'case': [[], []],
		'expected': True,
	},
	{
		'case': [[], [1]],
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
