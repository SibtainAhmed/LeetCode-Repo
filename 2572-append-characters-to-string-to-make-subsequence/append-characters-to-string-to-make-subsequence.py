class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        it=0
        for i in s:
            if i==t[it]:
                it+=1
            if it>=len(t):
                return 0    
        return len(t)-it


        