class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def setZero():
            for k in vowels.keys():
                vowels[k] = 0
        vowels = {alpha:0 for alpha in 'aeiou'}
        def checkMe():
            if vowels['a'] and vowels['e'] and vowels['i'] and vowels['o'] and vowels['u']:
                return True
            return False
        def checkCount(c):
            i = j = cons = res = 0
            while True:
                if checkMe() and cons >= c:
                    res += len(word) - j + 1
                    w = word[i]
                    if w in vowels:
                        vowels[w] -= 1
                    else: cons -= 1
                    i += 1
                else:
                    if j>=len(word): 
                        break
                    w = word[j]
                    if w in vowels:
                        vowels[w] += 1
                    else: cons += 1
                    j += 1
            return res
        a = checkCount(k)
        setZero()
        b = checkCount(k+1)
        return a - b