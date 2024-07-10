class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for cur in logs:
            if cur == './':
                continue
            elif cur == '../':
                res = max(0 , res-1)
            else:
                res += 1
        return res