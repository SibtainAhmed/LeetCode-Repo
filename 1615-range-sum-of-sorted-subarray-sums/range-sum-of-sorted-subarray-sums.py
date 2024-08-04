class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        # def subArrSum(sm, i):
        #     if i+1>=len(nums):
        #         res.append(sm)
        #         return
        #     else:
        #         res.append(sm)
        #         subArrSum(sm+nums[i], i+1)
        # for i in range(len(nums)):
        #     subArrSum(nums[i], i+1)
        for i,v in enumerate(nums):
            val = v
            res.append(val)
            for j in range(i+1, len(nums)):
                val += nums[j]
                res.append(val)
        res.sort()
        # print(res)
        resVal = 0
        mod = pow(10,9)+7
        for j in range(left-1,right):
            resVal += res[j]
            resVal %= mod
        return resVal