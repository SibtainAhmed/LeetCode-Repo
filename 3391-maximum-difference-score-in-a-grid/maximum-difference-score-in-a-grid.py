class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = -inf
        for r in range(m):
            for c in range(n):
                minPre = min(grid[r-1][c] if r else inf,
                grid[r][c-1] if c else inf)
                res = max(res, grid[r][c]-minPre)
                grid[r][c] = min(grid[r][c], minPre)
        return res
        
