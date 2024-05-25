class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = {w for w in wordDict}
        res =[]

        # def validString(st):
        #     lst = st.split(' ')
        #     for w in lst:
        #         if w not in words:
        #             return
        #     res.append(st)
        def join(st,w):
            if not st:
                return w
            return st+' '+w

        def dfs(i,st, word):
            if i>=len(s):
                if word in words:
                    nonlocal res
                    res.append(join(st,word))
                # validString(st)
            else:
                if word in words:
                    dfs(i+1, st, word+s[i])
                    dfs(i+1, join(st,word), s[i])
                else:
                    dfs(i+1, st, word+s[i])
                    
        dfs(0,'','')
        return res
