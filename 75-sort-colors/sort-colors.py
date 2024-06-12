class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = i = 0
        r = len(nums)-1
        while i<=r:
            val = nums[i]
            if val == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif val == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            else:
                i+=1
        