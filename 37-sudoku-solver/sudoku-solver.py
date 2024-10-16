class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)
        count = 0
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(int(board[r][c]))
                    cols[c].add(int(board[r][c]))
                    grid[((r//3)*3)+(c//3)].add(int(board[r][c]))

        def backtrack(r,c):
            if r==9: return True
            if c == 9: return backtrack(r+1, 0)
            elif board[r][c] != '.':
                return  backtrack(r,c+1)
            else:
                for i in range(1,10):
                    # print(r,c, (((r//3)*3)+(c//3)), end='; ')
                    if (i not in rows[r]) and (i not in cols[c]) and (i not in grid[((r//3)*3)+(c//3)]):
                        rows[r].add(i)
                        cols[c].add(i)
                        grid[((r//3)*3)+(c//3)].add(i)
                        board[r][c] = str(i)
                        if backtrack(r,c+1): return True
                        board[r][c] = '.'
                        rows[r].remove(i)
                        cols[c].remove(i)
                        grid[((r//3)*3)+c//3].remove(i)
                return False
        
        backtrack(0,0)