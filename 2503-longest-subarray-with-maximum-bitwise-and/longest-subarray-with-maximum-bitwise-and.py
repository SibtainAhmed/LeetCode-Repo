class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ln = ind = 0
        while ind < len(nums):
            if nums[ind] == mx:
                curr = 0
                while ind < len(nums) and nums[ind] == mx :
                    curr += 1
                    ind += 1
                ln = max(ln, curr)
            ind += 1
        return ln