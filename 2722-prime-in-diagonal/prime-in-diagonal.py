class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(n):
            if n==1: return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        n = len(nums)
        res = 0
        ind = 0
        for r in range(n):
            if isPrime(nums[r][ind]):
                res = max(res, nums[r][ind])
            if isPrime(nums[r][n-ind-1]):
                res = max(res, nums[r][n-ind-1])
            ind += 1
        return res