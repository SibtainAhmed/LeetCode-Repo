class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        st  = 0
        for end in range(len(nums)):
            target -= nums[end]
            while target<=0 and st<end+1:
                res = min(res, end-st+1)
                target += nums[st]
                st += 1
        return 0 if res == len(nums)+1 else res
