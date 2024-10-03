class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefS = 0
        pSum = [prefS:=prefS+val for val in nums]
        if prefS < p: return -1
        reqSum = prefS % p
        if not(reqSum): return 0
        rem = defaultdict(int)
        rem[0] = -1
        res = len(nums)+1
        for i,val in enumerate(pSum):
            cur = val%p
            key = (cur-reqSum+p)%p
            if key in rem:
                print(i, cur, val)
                res = min(res, i-rem[key])
            rem[cur] = i
        
        return res if res<len(nums) else -1


        # if sum(nums)<p:return -1
        # rem = [val%p for val in nums]
        # sm = sum(rem)
        # print(rem, sm)
        # if not(sm%p):return 0
        # res = math.inf
        # for i in range(len(nums)):
        #     reqVal = sm%p
        #     print(reqVal)
        #     val = 0
        #     for j in range(i,min(i+res, len(nums))):
        #         val += rem[j]
        #         if not(val%reqVal):
        #             if not(sm-val) and (sm-val) % p: continue
        #             print(bool(sm-val), 'sm-val')
        #             print(val, i)
        #             res = min(res,j-i+1)
        #             break
        # return res if res<=len(nums) else -1