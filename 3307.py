class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        jump = 0
        num = k

        while num > 1:
            lo_range = int(math.log2(num))
            hi_range = lo_range + 1

            border = 1 << lo_range

            if border == num:
                lo_range -= 1
                border = 1 << lo_range

            ind = lo_range

            num -= border

            if operations[ind] == 1:
                jump += 1

        return chr(ord('a') + (jump % 26))