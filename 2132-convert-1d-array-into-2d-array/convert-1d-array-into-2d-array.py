class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n: return []
        res = []
        for r in range(m):
            temp = []
            for c in range(n):
                temp.append(original[r*n + c])
            res.append(temp)
        return res