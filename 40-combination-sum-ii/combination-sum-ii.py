class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        temp = []
        def dfs(idx,sm):            
            if sm > target: return
            elif sm == target:
                res.append(temp.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                dfs(i+1, sm+candidates[i])
                temp.pop()
            # elif i >=len(candidates):
            #     return
            # else:
            #     dfs(i+1, sm, candidates[i])
            #     if prev != candidates[i]: wrong approach
            #         temp.append(candidates[i])
            #         dfs(i+1, sm+candidates[i], candidates[i])
            #         temp.pop()
            #     return
        
        dfs(0,0)
        return res