class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix), len(matrix[0])
        mem = {}
        # totalSquares = 0
        def countSubMatrixSquare(r,c):
            if r >= m or c>= n:
                return 0
            elif (r,c) in mem:
                return mem[(r,c)]
            elif matrix[r][c] == 0:
                return 0
            right = countSubMatrixSquare(r, c+1)
            bottom = countSubMatrixSquare(r+1, c)
            diagonal = countSubMatrixSquare(r+1, c+1)
            mem[(r,c)] = min(right, bottom, diagonal)+1
            return mem[(r,c)]
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c]:
                    matrix[r][c] = countSubMatrixSquare(r,c)
        # print(matrix)
        return sum([sum(m) for m in matrix])