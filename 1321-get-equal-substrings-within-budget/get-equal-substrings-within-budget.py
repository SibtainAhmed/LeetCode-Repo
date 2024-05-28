class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # @lru_cache
        # def dfs(i, remCost):
        #     if remCost < 0: return -1
        #     if i >= len(s):
        #         return 0
        #     if s[i] == t[i]:
        #         val = dfs(i+1, remCost)
        #     else:
        #         val = dfs(i+1, remCost-abs((ord(s[i])-ord(t[i]))))
        #     return val + 1
        aux = []
        for i in range(len(s)):
            aux.append(abs(ord(s[i])-ord(t[i])))
        res = curCost = st = 0
        e = 0
        while e<len(s):
            if curCost <= maxCost:
                curCost += aux[e]
                res = max(res, e-st)
                e += 1
            else:
                curCost -= aux[st]
                st+=1
        if curCost <= maxCost:
            res = max(res, e-st)
        return res