class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p = [0] * (n+1)
        for i in range(n):
            p[i+1] = p[i] + nums[i]
        print(p)
        dq = deque()
        m = float('inf')
        for i in range(n+1):
            while dq and p[i] - p[dq[0]] >= k:
                m = min(m, i - dq.popleft())
            while dq and p[i] <= p[dq[-1]]:
                dq.pop()
            dq.append(i)
        return m if m != float('inf') else -1