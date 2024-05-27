class Solution:
    def specialArray(self, nums: List[int]) -> int:
        ln = len(nums)
        cntArray = [0]*(ln+1)
        for v in nums:
            if v>=ln:
                cntArray[-1] += 1
            else:
                cntArray[v] += 1
        # print(cntArray)
        val = 0
        for i in range(ln,-1,-1):
            val += cntArray[i]
            if val > i:
                return -1
            elif val == i:
                return i
        return -1