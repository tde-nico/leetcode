from typing import Counter

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        c = Counter(arr)
        s = set()
        for v in c.values():
            if v in s:
                return False
            else:
                s.add(v)
        return True
