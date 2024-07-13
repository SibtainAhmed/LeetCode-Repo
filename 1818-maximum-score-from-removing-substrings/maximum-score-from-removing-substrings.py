class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        f = 'ab' if x>y else 'ba'
        ss = 'ba' if x>y else 'ab'
        fN, sN = max(x,y), min(x,y)
        i = 0
        while i<=len(s)-2:
            if s[i:i+2] == f:
                res += fN
                # i += 2
                s = s[:i] + s[i+2:]
                # print(s)
                i -= 1
            else:
                i+=1
        i = 0
        while i<=len(s)-2:
            if s[i:i+2] == ss:
                res += sN
                # i += 2
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i+=1
        return res
        