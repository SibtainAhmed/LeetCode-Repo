class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        n = [i for i in range(1,n+1)]
        currIndx = remIndx = 0
        while len(n)>1:
            remIndx = (currIndx + k -1)%len(n)
            n.pop(remIndx)
            currIndx = remIndx if len(n)>remIndx else 0
        return n[0]