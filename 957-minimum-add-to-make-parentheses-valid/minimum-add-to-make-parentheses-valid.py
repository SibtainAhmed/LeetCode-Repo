class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        op = cl = 0
        for br in s:
            if br == ')':
                if op:
                    op -= 1
                else:
                    cl += 1
            else:
                op += 1
        return op+cl