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
	output = s.replaceValueInTree(root)
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	out = build_tree(expected, 0, len(expected))
	def treecmp(r1, r2):
		if not r1 and not r2:
			return True
		if not r1 or not r2:
			return False
		return r1.val == r2.val and treecmp(r1.left, r2.left) and treecmp(r1.right, r2.right)
	assert treecmp(output, out)
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [5,4,9,1,10,None,7],
		'expected': [0,0,0,7,7,None,11],
	},
	{
		'case': [3,1,2],
		'expected': [0,0,0],
	},
]

if __name__ == '__main__':
	main()
