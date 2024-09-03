class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = 0
        for alpha in s:
            val = ord(alpha) - ord('a') + 1
            if val > 9:
                res += (val // 10)
            res += val % 10
        for _ in range(k-1):
            fRes = 0
            while res:
                fRes += res % 10
                res = res // 10
            res = fRes
        return res