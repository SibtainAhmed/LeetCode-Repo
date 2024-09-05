class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sm = mean*(n+m)
        rem = sm - sum(rolls)
        if rem > 6*n or rem<n: return []
        res = [rem//n]*n
        div = rem%n
        for i in range(div):
            res[i] += 1
        return res