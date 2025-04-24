class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        for i, c in enumerate(s):
            if i > 1 and c == res[-1] and c == res[-2]:
                continue
            res += c
        return res
