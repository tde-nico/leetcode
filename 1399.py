class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_count = {}
        max_size = 0

        for i in range(1, n + 1):
            s = sum(map(int, str(i)))
            digit_count[s] = digit_count.get(s, 0) + 1
            max_size = max(max_size, digit_count[s])

        return sum(1 for count in digit_count.values() if count == max_size)