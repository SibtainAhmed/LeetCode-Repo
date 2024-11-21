class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        totalCells = m*n-len(guards)-len(walls)
        grid = [[0]*n for _ in range(m)]
        for i,j in guards:
            grid[i][j] = 2
        for i,j in walls:
            grid[i][j] = 2
        for i,j in guards:
            for k in range(i+1,m):
                if not(grid[k][j]):
                    totalCells -= 1
                    grid[k][j] = 1
                elif grid[k][j] == 2: break
            for k in range(i-1,-1,-1):
                if not(grid[k][j]):
                    totalCells -= 1
                    grid[k][j] = 1
                elif grid[k][j] == 2: break
            for k in range(j+1,n):
                if not(grid[i][k]):
                    totalCells -= 1
                    grid[i][k] = 1
                elif grid[i][k] == 2: break
            for k in range(j-1,-1,-1):
                if not(grid[i][k]):
                    totalCells -= 1
                    grid[i][k] = 1
                elif grid[i][k] == 2: break
        # print(grid)
        return totalCells