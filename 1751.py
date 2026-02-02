class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[-1] * (k + 1) for _ in range(n)]

        def func(ind: int, cnt: int, last: int) -> int:
            if cnt == k or ind == n:
                return 0

            if dp[ind][cnt] != -1:
                return dp[ind][cnt]

            st, end, val = events[ind]

            take = 0
            if st > last:
                l, r = ind, n - 1
                ans = n
                while l <= r:
                    mid = (l + r) // 2
                    if events[mid][0] > end:
                        ans = mid
                        r = mid - 1
                    else:
                        l = mid + 1

                take = val + func(ans, cnt + 1, end)

            notTake = func(ind + 1, cnt, last)
            dp[ind][cnt] = max(take, notTake)
            return dp[ind][cnt]

        return func(0, 0, 0)