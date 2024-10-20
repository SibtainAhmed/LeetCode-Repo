class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res = ['a']
        cur = 'a'
        
        while cur != target and len(cur) <= len(target):
            if cur[-1] != target[len(cur)-1]:
                cur = cur[:len(cur)-1] + chr(ord(cur[len(cur)-1])+1)
            else:
                cur = cur + 'a'
            # print(cur)
            res.append(cur)
        return res