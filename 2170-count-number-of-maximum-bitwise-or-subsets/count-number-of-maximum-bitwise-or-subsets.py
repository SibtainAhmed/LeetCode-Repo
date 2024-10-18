class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0
        res = 0
        for n in nums:
            maxOr |= n
        
        def checkMaxValid(lst):
            if all(lst):return True
            return False
        
        def backtrack(val,indx):
            if val == maxOr:
                return 2**(len(nums)-indx)
            elif indx == len(nums):
                return 0
            else:
                val = backtrack(val|nums[indx], indx+1) + backtrack(val, indx+1)
                return val
        return backtrack(0,0)