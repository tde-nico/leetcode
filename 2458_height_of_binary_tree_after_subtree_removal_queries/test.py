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
	output = s.treeQueries(build_tree(case[0], 0, len(case[0])), case[1])
	print(f'Input: {case} Output: {output}, Expected: {expected}')
	assert output == expected
	print('Passed')


def main():
	for case in cases:
		test(case['case'], case['expected'])

cases = [
	{
		'case': [[1,3,4,2,None,6,5,None,None,None,None,None,7], [4]],
		'expected': [2],
	},
	{
		'case': [[5,8,9,2,1,3,7,4,6], [3,2,4,8]],
		'expected': [3,2,3,2],
	},
]

if __name__ == '__main__':
	main()
