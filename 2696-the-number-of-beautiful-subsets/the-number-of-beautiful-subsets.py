class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        def dfs(i, lst):
            if i>=len(nums):
                nonlocal res
                res += 1
                return
            dfs(i+1, lst)
            flag = True
            for val in lst:
                if nums[i] - val == k: flag = False
            if flag:
                dfs(i+1, lst+[nums[i]])

        for i,v in enumerate(nums):
            dfs(i+1, [v])
        return res