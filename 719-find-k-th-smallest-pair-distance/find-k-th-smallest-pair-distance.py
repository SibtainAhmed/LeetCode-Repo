class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def checkPairs(diff):
            sP = eP = cnt = 0
            while eP < len(nums):
                # while nums[eP] - nums[sP] <= diff and eP < len(nums):
                while nums[eP] - nums[sP] > diff:
                    sP += 1
                cnt += eP - sP
                eP += 1
            return cnt

        nums.sort()
        # n = len(nums)
        st,ed = 0, nums[-1] - nums[0]
        mid = 0
        # i = 0
        while True:
            # i += 1
            mid = (st + ed)//2
            check = checkPairs(mid)
            if st == ed: return mid
            elif check >= k:
                ed = mid
            else:
                st = mid + 1
        return 100000
            # if k >= 1+((n*(mid-1))//2) and k <= (n*(mid)/2):
            #     print('break',1+((n*(mid-1))/2) , (n*(mid)/2) )
            #     break
            # elif k < 1+((n*(mid-1))/2):
            #     print('\n1+(n*(mid-1)/2) = ',((n*(mid-1))/2))
            #     print('first')
            #     print('st = ', st, ', ed =', ed)
            #     ed = mid
            # else:
            #     print('\nsecond')
            #     print('--- st = ', st, ', ed =', ed)
            #     st = mid+1
        
        # stIdx = ((n*(mid-1))/2)
        # print('mid = ', mid)
        # print('stIdx = ', stIdx)
        # for j in range(0,n-mid):
        #     stIdx += 1
        #     if stIdx == k:
        #         print(nums[j+mid] ,',', nums[j])
        #         return nums[j+mid] - nums[j]
        # print(stIdx)
        # return 100000