class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        for i in range(32):
            if (start>>i)%2 != (goal>>i)%2:
                res += 1
        return res