class Solution:
    def countAndSay(self, n: int) -> str:
        
        def countSay(n):
            if n == 1:
                return '1'
            else:
                val = countSay(n-1)
                res = ''
                cnt = 1
                for r in range(len(val)-2,-1,-1):
                    if val[r] ==val[r+1]:
                        cnt += 1
                    else:
                        res = str(cnt)+ val[r+1] + res
                        cnt = 1
                return str(cnt)+ val[0] + res
        return countSay(n)