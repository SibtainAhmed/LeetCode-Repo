class Solution:
    def scoreOfString(self, s: str) -> int:
        last = ord(s[0])
        res = 0
        for alpha in s:
            res += abs(last - ord(alpha))
            last = ord(alpha)
        return res