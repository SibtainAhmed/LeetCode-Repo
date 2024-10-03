class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # prefS = 0
        # pSum = [prefS:=prefS+val for val in nums]
        # if prefS < p: return -1
        reqSum = sum(nums) % p
        if not(reqSum): return 0
        # rem = defaultdict(int)
        rem = {0:-1}
        res = len(nums)+1
        cur = 0
        for i,val in enumerate(nums):
            cur = (cur+val)%p
            key = (cur-reqSum+p)%p
            if key in rem:
                print(i, cur, val)
                res = min(res, i-rem[key])
            rem[cur] = i
        
        return res if res<len(nums) else -1

