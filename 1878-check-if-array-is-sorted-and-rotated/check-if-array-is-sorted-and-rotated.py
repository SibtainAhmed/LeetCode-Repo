class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[j-1]:
                count += 1
        return count<=1