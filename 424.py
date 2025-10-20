class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mx = 0
        f = {}
        for r in range(len(s)):
            f[s[r]] = f.get(s[r], 0) + 1
            mx = max(mx, f[s[r]])
            if r - l + 1 - mx > k:
                f[s[l]] -= 1
                l += 1
        return len(s) - l