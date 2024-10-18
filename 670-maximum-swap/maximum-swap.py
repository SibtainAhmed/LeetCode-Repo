class Solution:
    def maximumSwap(self, num: int) -> int:
        nString = [n for n in str(num)]
        for l in range(len(nString)):
            # val = (nString[l])
            mxIndx = l
            for r in range(len(nString)-1,l,-1):
                if int(nString[r]) > int(nString[mxIndx]):
                    mxIndx = r
            if mxIndx != l:
                nString[l], nString[mxIndx] = nString[mxIndx], nString[l]
                return int(''.join(nString))
        return int(''.join(nString))
