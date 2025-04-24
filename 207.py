import collections

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		indegree = [0] * numCourses
		adj = [[] for _ in range(numCourses)]
		for src, dst in prerequisites:
			adj[src].append(dst)
			indegree[dst] += 1
		
		q = collections.deque()
		for n in range(numCourses):
			if indegree[n] == 0:
				q.append(n)
		
		while q:
			node = q.popleft()
			numCourses -= 1
			for neighbor in adj[node]:
				indegree[neighbor] -= 1
				if indegree[neighbor] == 0:
					q.append(neighbor)
		
		return numCourses == 0