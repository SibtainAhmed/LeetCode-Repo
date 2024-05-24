class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for val in nums:
            temp = []
            while val>=1:
                temp.append(val%10)
                val = val//10
            temp.reverse()
            res.extend(temp)
        return res