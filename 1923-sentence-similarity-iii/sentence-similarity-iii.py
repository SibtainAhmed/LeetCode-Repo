class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2: return True
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        if len(s2) > len(s1):
            s1, s2 = s2, s1
        if len(s1) == 1:
            return False
        for st in range(len(s2)):
            if s1[st] != s2[st]:
                st -= 1
                break
        st += 1
        if st == len(s2): return True
        
        for ed in range(-1, -len(s2)-1, -1):
            print(s1[ed], s2[ed], ed)
            if s1[ed] != s2[ed]:
                ed += 1
                break
        if abs(ed) == len(s2): return True
        print(st + abs(ed), st, abs(ed))
        if len(s2) <= st + abs(ed):
            return True
        return False