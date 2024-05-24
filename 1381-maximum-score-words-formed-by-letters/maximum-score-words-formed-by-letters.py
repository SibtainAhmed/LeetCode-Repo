class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for l in letters:
            freq[l] += 1
        
        def checkWord(i):
            cntWord = Counter(words[i])
            for k in cntWord.keys():
                if cntWord[k] > freq[k]:
                    return False
            return True

        def removeWord(i):
            val = 0
            for w in words[i]:
                freq[w] -= 1
                val += score[ord(w)-97]
            return val
        def addWord(i):
            for w in words[i]:
                freq[w] += 1
        
        def dfs(i,tRes):
            if i>=len(words):
                nonlocal res
                # print('tRes ==> ', tRes)
                res = max(res, tRes)
            else:
                dfs(i+1, tRes)
                if checkWord(i):
                    # print('true checkword', words[i])
                    val = removeWord(i)
                    # print('val,i ==', val, i)
                    dfs(i+1, tRes+val)
                    addWord(i)
        dfs(0,0)
        return res