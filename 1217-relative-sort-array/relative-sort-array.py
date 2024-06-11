class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cntArr1 = Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num for _ in range(cntArr1[num])])
            del cntArr1[num]
        for resNum in sorted(cntArr1.keys()):
            res.extend([resNum for _ in range(cntArr1[resNum])])
        return res