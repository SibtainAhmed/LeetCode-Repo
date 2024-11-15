class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort() 
        ans = 0 
        for i in range(len(nums)-1):
            num = nums[i]
            if max(num*2, num+nums[i+1])>upper:
                break
            x = bisect_left(nums, lower-num) 
            y = bisect_right(nums, upper-num) - 1
            if x <= i:
                x = i+1
            if x > y: continue
            ans += y - x + 1 
        return ans