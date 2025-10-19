class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        if c1 == c2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            c2[s2[r]] = c2.get(s2[r], 0) + 1
            c2[s2[l]] -= 1
            if c2[s2[l]] == 0:
                del c2[s2[l]]
            l += 1
            if c1 == c2:
                return True

        return False