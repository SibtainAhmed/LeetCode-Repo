class Solution:
    def minimumSteps(self, s: str) -> int:
        l, r= 0,0
        res = 0
        while r<len(s):
            while r<len(s) and s[r] == '1':
                r += 1
            if r>=len(s): return res
            res += (r-l)
            l += 1
            r += 1
        return res