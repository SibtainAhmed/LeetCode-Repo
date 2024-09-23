class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictSet = {d for d in dictionary}
        mem = {}
        def dfs(string):
            if string in dictSet:
                return 0
            elif len(string) == 1:
                return 1
            elif string in mem:
                return mem[string]
            else:
                mn = len(string)
                for i in range(1,len(string)):
                    mn = min(mn, dfs(string[:i]) + dfs(string[i:]))
                mem[string] = mn
                return mn
        
        return dfs(s)