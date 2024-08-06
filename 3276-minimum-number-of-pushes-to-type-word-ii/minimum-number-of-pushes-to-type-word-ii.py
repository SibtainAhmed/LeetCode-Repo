class Solution:
    def minimumPushes(self, word: str) -> int:
        wordCnt = Counter(word)
        Cnt = [c for c in wordCnt.values()]
        Cnt.sort(reverse=True)
        # Cnt = wordCnt.values()
        # reversed(Cnt)
        res = 0
        for i in range(len(Cnt)):
            res += Cnt[i]*(1+(i//8))
            # print(res)
        # print(Cnt)
        return res