class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        # nums.sort(reverse=True)
        res = len(nums)+1
        st = end = 0
        # print(res)
        while end<len(nums):
            # while end<len(nums) and target > 0:
            target -= nums[end]
            end += 1
            # if target<=0:
            #     res = min(res, end-st)
            while target<=0 and st<end:
                res = min(res, end-st)
                target += nums[st]
                st += 1
            # if target<=0:
            #     res = min(res, end-st)
        return res
