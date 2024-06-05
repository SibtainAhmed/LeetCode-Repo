class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        smallest = Counter(min(words, key=lambda x: len(x)))
        for large in words:
            largeCnt = Counter(large)
            for k,v in smallest.items():
                if k in largeCnt:
                    smallest[k] = min(largeCnt[k], v)
                else:
                    smallest[k] = 0
        res = []
        for k,v in smallest.items():
            for _ in range(v):
                res.append(k)
        return res