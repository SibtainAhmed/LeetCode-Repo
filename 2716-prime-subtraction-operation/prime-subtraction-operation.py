class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        mxVal = max(nums)
        primes = [0]
        for i in range(2,min(mxVal+1, 1000)):
            flag = True
            for j in range(2, math.ceil(math.sqrt(i))+1):
                if i == j: continue
                if i%j == 0:
                    flag = False
                    break
            if flag:
                primes.append(i)
        def findPrime(val, lastVal):
            left, right = 0, len(primes)-1
            while right > left:
                mid = ((left + right)//2)+1
                if val - primes[mid] > lastVal:
                    left = mid
                else:
                    right = mid -1
            right = max(0,right)
            return primes[right] if (abs(val - primes[right]) > lastVal) else -1



        lastVal = 0
        for i in range(len(nums)):
            n = nums[i]
            val = findPrime(n,lastVal)
            if val == -1: 
                return False
            lastVal = n - val
            nums[i] = lastVal
        return True