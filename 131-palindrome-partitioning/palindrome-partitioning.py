class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindromeCheck(st):
            print(st)
            end = -1
            for start in range(len(st)//2 + 1):
                if st[start] != st[end]:
                    return False
                end -= 1
            return True
        def dfs(newSt):
            if not newSt:return [[]]
            tempRes = []
            for i in range(len(newSt)):
                var = palindromeCheck(newSt[:i+1])
                if var:
                    word = newSt[:i+1]
                    tempRes.extend([[word]+lst for lst in dfs(newSt[i+1:])])
            return tempRes
        return dfs(s)