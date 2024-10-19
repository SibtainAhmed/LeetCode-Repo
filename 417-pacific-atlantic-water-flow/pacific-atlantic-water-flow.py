class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited = set()
        results = set()
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        records = {}
        m, n = len(heights), len(heights[0])

        def dfs(r,c, pVal):
            if (r,c) in visited:
                return [False, False]
            elif r==m or c==n:
                return [True, False]
            elif r==-1 or c==-1:
                return [False, True]
            elif pVal < heights[r][c]: 
                return [False, False]
            elif (r,c) in results:
                return [True, True]
            # elif (r,c) in records:
            #     return records[(r,c)]
            val = [False, False]
            visited.add((r,c))
            for dr,dc in directions:
                temp = dfs(r+dr, c+dc, heights[r][c])
                val = [temp[0]|val[0], temp[1]|val[1]]
                if val[0] and val[1]:
                    results.add((r,c))
                    break
            visited.remove((r,c))
            # records[(r,c)] = val
            return val
        
        for r in range(m):
            for c in range(n):
                dfs(r,c,heights[r][c])
        print(records)
        return [[r,c] for r,c in results]