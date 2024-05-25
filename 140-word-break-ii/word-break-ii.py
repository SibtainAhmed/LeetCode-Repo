class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = {w for w in wordDict}
        res =[]

        def validString(st):
            # print(st)
            lst = st.split(' ')
            for w in lst:
                if w not in words:
                    return
            # print('true')
            res.append(st)

        def dfs(i,st):
            if i>=len(s):
                validString(st)
            else:
                dfs(i+1, st+s[i])
                dfs(i+1, st+' '+s[i])
                # dfs(i+1, st+' ')
        dfs(0,'')
        return res
