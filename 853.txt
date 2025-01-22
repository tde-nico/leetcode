class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        for p, s in sorted([(p, s) for p, s in zip(position, speed)]):
            t = (target - p) / s
            while st and t >= st[-1]:
                st.pop()
            st.append(t)
        return len(st)
        