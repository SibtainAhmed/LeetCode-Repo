class Solution:
    def minTimeToReach(self, grid: List[List[int]]) -> int:
        m, n = len(grid)-1, len(grid[0])-1
        visited = {(0,0)}
        heap = [(0,0,0)]
        direct = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            time,r,c = heapq.heappop(heap)
            if (r,c) == (m,n): return time
            for rd,cd in direct:
                nR, nC = r+rd, c+cd
                if (0<=nR<=m and 0<=nC<=n) and (nR,nC) not in visited:
                    visited.add((nR,nC))
                    heapq.heappush(heap, (max(time,grid[nR][nC])+1,nR,nC))
        return -1