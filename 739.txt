class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                index = s.pop()
                res[index] = i - index
            s.append(i)
        return res
        