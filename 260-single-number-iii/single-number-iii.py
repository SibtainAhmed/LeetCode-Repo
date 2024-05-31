class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        mapp = defaultdict(int)
        for i in nums:
            mapp[i] += 1
        for k,v in mapp.items():
            if v==1: res.append(k)
        return res