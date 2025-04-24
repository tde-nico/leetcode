class Solution:
	def countSquares(self, matrix: List[List[int]]) -> int:
		n = len(matrix)
		m = len(matrix[0])
		dp = [[0] * m for _ in range(n)]
		res = 0
		for y in range(n):
			dp[y][0] = matrix[y][0]
			res += matrix[y][0]
		for x in range(1, m):
			dp[0][x] = matrix[0][x]
			res += matrix[0][x]
		for y in range(1, n):
			for x in range(1, m):
				if matrix[y][x] == 1:
					dp[y][x] = 1 + min(dp[y][x-1], dp[y-1][x], dp[y-1][x-1])
				res += dp[y][x]
		return res
