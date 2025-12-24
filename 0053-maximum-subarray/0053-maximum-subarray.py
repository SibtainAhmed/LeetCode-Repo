class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        res = nums[0]
        for v in nums:
            maxSum += v
            res = max(maxSum, res)
            if maxSum < 0:
                maxSum = 0
        return res