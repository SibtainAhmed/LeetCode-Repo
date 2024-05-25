class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        boolArray = [False]*(len(s)+1)
        boolArray[-1] = True
        for i in range(len(s)-1 , -1,-1):
            for v in wordSet:
                if len(s)-i+1 >= len(v) and v == s[i:len(v)+i]:
                    if boolArray[i+len(v)]:
                        boolArray[i] = boolArray[i+len(v)]
                        break
        # print(boolArray)
        return boolArray[0]