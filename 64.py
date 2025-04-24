class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		rows = len(grid)
		cols = len(grid[0])
		for y in range(rows):
			for x in range(cols):
				if y == 0:
					if x == 0:
						continue
					grid[y][x] += grid[y][x-1]
				else:
					if x == 0:
						grid[y][x] += grid[y-1][x]
					else:
						grid[y][x] += min(grid[y][x-1], grid[y-1][x])
		return grid[-1][-1]
