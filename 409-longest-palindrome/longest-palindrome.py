class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        res = odd = 0
        for v in cnt.values():
            if v%2:
                if odd:
                    res += odd - 1
                odd = v
            else:
                res += v
        return res + odd