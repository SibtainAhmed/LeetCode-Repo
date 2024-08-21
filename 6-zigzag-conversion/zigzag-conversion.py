class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = []
        # print(numRows*2-2, 'jump')
        for k in range(0,len(s),numRows*2-2):
            res.append(s[k])
        for i in range(1,numRows-1):
            for j in range(i,len(s),numRows*2-2):
                res.append(s[j])
                val = numRows - ((j) % (numRows-1)) -1
                # print(val)
                if j+val+val < len(s):
                    res.append(s[j+val+val])            
        for k in range(numRows-1,len(s),numRows*2-2):
            res.append(s[k])
        return ''.join(res)