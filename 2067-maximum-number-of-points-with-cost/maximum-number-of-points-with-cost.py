class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        left = [0]*n
        right = [0]*n
        for r in range(m-1):
            for c in range(n):
                if c:
                    left[c] = max(left[c-1]-1, points[r][c])
                    right[n-1-c] = max(right[n-c]-1, points[r][n-1-c])
                else:
                    left[c] = points[r][c]
                    right[n-c-1] = points[r][n-1-c]
            for c in range(n):
                points[r+1][c] = max(right[c],left[c])+points[r+1][c]
            # print(points[r+1])
        return max(points[-1])