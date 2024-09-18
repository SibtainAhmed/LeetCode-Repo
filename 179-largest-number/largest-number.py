class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        def compareIt(x,y):
            if x+y > y+x:
                return -1
            else: return 1
        res = sorted(nums, key=cmp_to_key(compareIt))
        return str(int("".join(res)))
        # if nums == [34323,3432]:
        #     return "343234323"
        # mx = max(nums)
        # i,j = 1,10
        # while mx >= j:
        #     j *= 10
        #     i += 1 
        # res = []
        # for n in nums:
        #     n = str(n)
        #     ln = len(n)
        #     last = n[-1]
        #     res.append([-int(n+(i-ln)*last), i-ln])
        # heapq.heapify(res)
        # ret = ''
        # for _ in range(len(nums)):
        #     n, k = heapq.heappop(res)
        #     # n = -n
        #     ret = ret + str(-n//(10**k))
        # return str(int(ret))

              