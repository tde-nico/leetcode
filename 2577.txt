class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m = len(grid)
        n = len(grid[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        min_heap = [(0, 0, 0)]
        min_time = [[float('inf')] * n for _ in range(m)]
        while min_heap:
            t, y, x = heapq.heappop(min_heap)
            if y == m-1 and x == n-1:
                return t
            
            for dy, dx in dirs:
                new_y = y + dy
                new_x = x + dx
                if new_y < 0 or new_y >= m or new_x < 0 or new_x >= n or min_time[new_y][new_x] != float('inf'):
                    continue

                if grid[new_y][new_x] <= t+1 and t+1 <= min_time[new_y][new_x]:
                        min_time[new_y][new_x] = t+1
                        heapq.heappush(min_heap, (t+1, new_y, new_x))
                    
                diff = grid[new_y][new_x] - t
                if diff % 2:
                    new_t = grid[new_y][new_x]
                else:
                    new_t = grid[new_y][new_x] + 1

                if grid[new_y][new_x] > t+1 and new_t < min_time[new_y][new_x]:
                    min_time[new_y][new_x] = new_t
                    heapq.heappush(min_heap, (new_t, new_y, new_x))
        
        return -1
        