class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        st = set()
        def dfs(i, string, currSet):
            if i >= len(string):
                if not(string):
                    return len(currSet)
                if string in currSet:
                    return 0
                else:
                    return len(currSet)+1
            else:
                val = 0
                if string[:i+1] not in currSet:
                    currSet.add(string[:i+1])
                    val = max(val, dfs(0,string[i+1:],currSet))
                    currSet.remove(string[:i+1])
                val = max(val, dfs(i+1,string, currSet))
                return val
        return dfs(0,s,st)