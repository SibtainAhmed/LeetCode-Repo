class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)-1
        visited = {(0,0)}
        heap = [(grid[0][0],0,0)]
        direct = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            time,r,c = heapq.heappop(heap)
            if (r,c) == (n,n): return time
            for rd,cd in direct:
                nR, nC = r+rd, c+cd
                if (0<=nR<=n and 0<=nC<=n) and (nR,nC) not in visited:
                    visited.add((nR,nC))
                    heapq.heappush(heap, (max(time,grid[nR][nC]),nR,nC))
        return -1