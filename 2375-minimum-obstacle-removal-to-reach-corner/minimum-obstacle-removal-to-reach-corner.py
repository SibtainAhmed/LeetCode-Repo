class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q = deque()
        q.append((0,0,0))
        visited = {(0,0)}
        m, n = len(grid)-1, len(grid[0])-1
        direct = [(1,0),(0,1),(-1,0),(0,-1)]   

        while q:
            o,r,c = q.popleft()
            # print(q.popleft())
            if (r,c) == (m,n): return o
            for rd,cd in direct:
                nR, nC = r+rd, c+cd
                if (0<=nR<=m and 0<=nC<=n) and (nR,nC) not in visited:
                    visited.add((nR,nC))
                    nO = o + grid[nR][nC]
                    if q and nO >= q[-1][0]:
                        q.append((nO,nR,nC))
                    else:
                        q.appendleft((nO,nR,nC))
                