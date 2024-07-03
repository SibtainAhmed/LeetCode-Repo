class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        res = math.inf
        for l in range(4):
            r = len(nums)-4+l
            res = min(res, nums[r]-nums[l])
        return res