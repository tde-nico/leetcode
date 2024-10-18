import collections

class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		m = len(grid[0])
		n = len(grid)
		q = collections.deque()
		fresh = 0
		for y in range(n):
			for x in range(m):
				element = grid[y][x]
				if element == 2:
					q.append((y, x))
				elif element == 1:
					fresh += 1
		epoch = 0
		while fresh > 0 and q:
			for i in range(len(q)):
				y, x = q.popleft()
				neighbors = [
					(y+1, x), (y-1, x),
					(y, x+1), (y, x-1),
				]			  
				for ny, nx in neighbors:
					if (
						ny >= 0 and ny < n and
						nx >= 0 and nx < m and
						grid[ny][nx] == 1
					):
						grid[ny][nx] = 2
						q.append((ny, nx))
						fresh -= 1
			epoch += 1
		return epoch if fresh == 0 else -1
