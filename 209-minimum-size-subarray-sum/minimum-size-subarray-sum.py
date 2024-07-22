class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        res = len(nums)+1
        st  = 0
        for end in range(len(nums)):
            target -= nums[end]
            while target<=0 and st<end+1:
                res = min(res, end-st+1)
                target += nums[st]
                st += 1
        return res
