class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        for n in nums:
            while s:
                if gcd(s[-1], n) == 1:
                    break
                n = lcm(s.pop(), n)
            s.append(n)
        return s