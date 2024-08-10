class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = cnt = r = 0
        while r < len(nums):
            i = 0
            while r+i<len(nums) and nums[r+i] == nums[r]:
                i += 1
            for j in range(i):
                nums[l+j] = nums[r+j]
                # l += 1
            l += min(2,i)
            r += i
        # print(nums)
        return l


        # currCnt = nextCnt = 0
        # nextIndx = currIndx = 0
        # l = 0
        # print('len:', len(nums))
        # for r in range(len(nums)):
        #     print('\nloop', r)
        #     if nums[currIndx] == nums[r]:
        #         print('if: ',r)
        #         currCnt += 1
        #         if currCnt <= 3:
        #             l = r
        #             print('first:',l)
        #             # sortTill = l
        #     else:
        #         print('else: ', r)
        #         if nums[nextIndx] == nums[r]:
        #             nextCnt += 1
        #         else:
        #             nextIndx = r
        #             nextCnt = 1
        #         if currCnt >= 3:
        #             nums[l] = nums[r]
        #             currCnt -= 1
        #             l += 1
        #             print('second:',l)
        #             nextCnt += 1
        #         else:
        #             currCnt = nextCnt
        #             nextCnt = 0
        #             currIndx = nextIndx
        #             l += 1
        #         print(f'l={l}, currCnt={currCnt}, nextCnt={nextCnt}, nextIndx={nextIndx}')
        #     print(nums)
        # print(l)
        # return l
