class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)
        # robots * factories * maxCapacity
        dp = [[[float('inf')] * (n+1) for i in range(m)] for j in range(n)]
        
        robot.sort()
        factory.sort()
        
        for i in range(n):
            r = robot[i]
            for j in range(m):
                pos, cap = factory[j]
                other = dp[i][j-1][0] if j != 0 else float('inf')
                dp[i][j][cap] = other
                
                for k in range(cap-1, -1, -1):
                    f = abs(r-pos)+dp[i-1][j][k+1] if i != 0 else abs(r-pos)
                    dp[i][j][k] = min(other, f)

        return dp[-1][-1][0]
