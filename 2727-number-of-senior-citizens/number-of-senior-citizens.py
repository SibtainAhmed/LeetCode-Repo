class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for st in details:
            if int(st[11:13]) > 60:
                res += 1
        return res