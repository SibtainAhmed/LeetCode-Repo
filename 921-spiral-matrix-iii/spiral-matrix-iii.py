class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        currMove = 0
        while len(res) < rows*cols:
            currMove += 1
            for c in range(cStart, cStart+currMove):
                if c<cols and c>=0 and rStart<rows and rStart>=0:
                    res.append([rStart,c])
                else:
                    continue
            cStart = cStart + currMove
            for r in range(rStart, rStart+currMove):
                if r<rows and r>=0 and cStart<cols and cStart>=0:
                    res.append([r,cStart])
                else:
                    continue
            rStart = rStart + currMove

            for c in range(cStart, cStart-currMove-1, -1):
                if c<cols and c>=0 and rStart<rows and rStart>=0:
                    res.append([rStart,c])
                else:
                    continue
            cStart = c-1
            for r in range(rStart, rStart-currMove-1, -1):
                if r<rows and r>=0 and cStart<cols and cStart>=0:
                    res.append([r,cStart])
                else:
                    continue
            rStart = r-1
            currMove += 1
        return res