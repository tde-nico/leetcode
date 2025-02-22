class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, l = 0, len(str2)
        for c in str1:
            if i < l and (ord(str2[i]) - ord(c)) % 26 < 2:
                i += 1
        return i == l

        