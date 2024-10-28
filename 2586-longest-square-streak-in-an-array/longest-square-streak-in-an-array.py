class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        diction = {v:i for i,v in enumerate(nums)}

        for i in range(len(nums)):
            curr = nums[i]
            ln = 1
            while pow(curr,2) in diction:
                curr = nums[diction[pow(curr,2)]]
                ln += 1
                res = max(res, ln)
        return res if res else -1