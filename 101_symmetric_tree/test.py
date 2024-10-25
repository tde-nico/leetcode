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
	root = build_tree(case, 0, len(case))
	output = s.isSymmetric(root)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')

def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [1,2,2,3,4,4,3],
		'expected': True,
	},
	{
		'case': [1,2,2,None,3,None,3],
		'expected': False,
	},
]

if __name__ == '__main__':
	main()
