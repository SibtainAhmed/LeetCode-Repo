class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1)
        res = []
        for v in nums2:
            if cnt.get(v,0)>0:
                res.append(v)
                cnt[v] -= 1
        return res