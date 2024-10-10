class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        mx = -math.inf
        maxArr = [0]*len(nums)
        for i in range(len(nums)-1, -1,-1):
            n = nums[i]
            mx = max(mx, n)
            maxArr[i] = mx
        st = 0
        for ed in range(1,len(nums)):
            if maxArr[ed] >= nums[st]:
                res = max(res, ed-st)
            else:
                while ed >= st and maxArr[ed] < nums[st]:
                    st += 1
            # res = max(res, maxArr[i] - minArr[i])
        return res