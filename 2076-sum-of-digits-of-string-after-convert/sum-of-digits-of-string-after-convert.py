class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = 0
        for alpha in s:
            val = ord(alpha) - ord('a') + 1
            print(val)
            if val > 9:
                res += (val // 10)
            res += val % 10
            print('res = ', res)
        print(res)
        for _ in range(k-1):
            fRes = 0
            while res:
                fRes += res % 10
                res = res // 10
            res = fRes
            print(res)
        return res