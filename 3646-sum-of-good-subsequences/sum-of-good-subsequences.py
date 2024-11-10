class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        f = defaultdict(int)
        g = defaultdict(int)
        for n in nums:
            x = 1
            y = n
            for m in [n - 1, n + 1]:
                x += f[m]
                y += g[m] + f[m] * n
            f[n] = (f[n] + x) % mod
            g[n] = (g[n] + y) % mod
        # print(f)
        return sum(g.values()) % mod