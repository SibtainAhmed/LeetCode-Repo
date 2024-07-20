class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        res = [[0]*n for i in range(m)]

        for i in range(m):
            rSum = rowSum[i]
            for j in range(n):
                if rSum >= colSum[j]:
                    rSum -= colSum[j]
                    res[i][j] = colSum[j]
                    colSum[j] = 0
                else:
                    # print(f'[{i}][{j}] , rSum = {rSum}, colSum[{j}]={colSum[j]}')
                    res[i][j] = rSum
                    colSum[j] -= rSum
                    rSum = 0
                    break
            # print(colSum)
        return res