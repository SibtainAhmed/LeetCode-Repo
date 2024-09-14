class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        prefix = [0]
        for j in range(len(arr)):
            prefix.append(prefix[j]^arr[j])
        for i,u in queries:
            res.append(prefix[u+1]^prefix[i])
        return res