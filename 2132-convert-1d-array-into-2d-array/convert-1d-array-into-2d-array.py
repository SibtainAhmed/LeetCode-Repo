class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n: return []
        res = []
        for r in range(m):
            res.append(original[r*n:r*n+n])
        return res