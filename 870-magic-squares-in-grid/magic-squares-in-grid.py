class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checkMatrix(r,c):
            check = set()
            for ri in range(r,r+3):
                for ci in range(c,c+3):
                    val = grid[ri][ci]
                    if val and val<10:
                        check.add(val)
                    else: return 0
            if len(check) != 9:return 0 

            comp = sum(grid[r][c:c+3])
            if comp == sum(grid[r+1][c:c+3]) and comp == sum(grid[r+2][c:c+3]):
                if comp == grid[r][c]+grid[r+1][c]+grid[r+2][c] and comp == grid[r][c+1]+grid[r+1][c+1]+grid[r+2][c+1] and comp == grid[r][c+2]+grid[r+1][c+2]+grid[r+2][c+2]:
                    if comp == grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2] and comp == grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]:
                        return 1

            return 0

        res = 0
        for r in range(len(grid)-2):
            for c in range(len(grid[0])-2):
                res += checkMatrix(r,c)
                
        return res