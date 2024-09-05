class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sm = mean*(n+m)
        rem = sm - sum(rolls)
        # print('rem=', rem)
        if rem > 6*n or rem<n: return []
        res = []
        for i in range(n):
            val = min(6,rem-n+i+1)
            rem -= val
            res.append(val)
        return res