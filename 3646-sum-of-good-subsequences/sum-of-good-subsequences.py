class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        leftCnt = [0]*len(nums)
        rightCnt = [0]*len(nums)
        for i,n in enumerate(nums):
            leftCnt[i] = (f1[n+1] + f1[n-1] + 1)
            f1[n] = (leftCnt[i]% mod + f1[n]% mod) % mod
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            rightCnt[i] = (f2[n+1] + f2[n-1] + 1)
            f2[n] = (f2[n]% mod + rightCnt[i]% mod)% mod
        res = 0
        for k in range(len(nums)):
            # res += ((((leftCnt[k]% mod)*(rightCnt[k]% mod)% mod)*(nums[k]% mod))% mod)%mod
            res = (res + ((leftCnt[k]%mod* (rightCnt[k]%mod))%mod * nums[k])%mod)%mod
        return res