class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindromeCheck(st):
            return st == st[::-1]
        finalRes = []
        def dfs(newSt, tempRes):
            if not newSt:return finalRes.append(tempRes)
            for i in range(len(newSt)):
                if palindromeCheck(newSt[:i+1]):
                    word = newSt[:i+1]
                    dfs(newSt[i+1:], tempRes+[word])
        dfs(s,[])
        return finalRes