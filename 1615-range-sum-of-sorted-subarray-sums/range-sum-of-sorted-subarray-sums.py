class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        def subArrSum(sm, i):
            if i>=len(nums):
                res.append(sm)
                return
            else:
                res.append(sm)
                subArrSum(sm+nums[i], i+1)
        for i in range(len(nums)):
            subArrSum(nums[i], i+1)
       
        res.sort()
        # print(res)
        resVal = 0
        mod = pow(10,9)+7
        for j in range(left-1,right):
            resVal += res[j]
            resVal %= mod
        return resVal