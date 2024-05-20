class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        def dfs(i, total):
            if i>=n: return total 
            val = nums[i]^total
            return dfs(i+1,val) + dfs(i+1,total)
            
        return dfs(0,0)