class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(i,lst):
            if i>=n:
                res.append(lst)
                return
            dfs(i+1, lst)
            dfs(i+1, lst + [nums[i]])
        dfs(0,[])
        return res