class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = res = 0
        prefix = {00000:-1}
        st = {'a':1,'e':2,'i':4,'o':8,'u':16}
        for i, alpha in enumerate(s):
            if alpha in st:
                mask ^= st[alpha]
            if mask in prefix:
                res = max(res, i-prefix[mask])
            else:
                prefix[mask] = i
        return res
        