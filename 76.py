class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(t) > len(s):
            return ""
        
        w, ct = {}, Counter(t)
        seq, mn = (-1, -1), float('inf')
        have, need = 0, len(ct)
        l = 0
        for r, c in enumerate(s):
            w[c] = w.get(c, 0) + 1
            if c in ct and w[c] == ct[c]:
                have += 1
            
            while have == need:
                if r-l+1 < mn:
                    seq = (l, r)
                    mn = r-l+1
                w[s[l]] -= 1
                if s[l] in ct and w[s[l]] < ct[s[l]]:
                    have -= 1
                l += 1

        return s[seq[0]:seq[1]+1] if mn != float('inf') else ""
