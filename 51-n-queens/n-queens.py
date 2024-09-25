import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        tempRes = []
        temp =[['.']*n for _ in range(n)]
        def newArr(arr,i,row):
            arrC = copy.deepcopy(arr)
            arrC[row][i] = 'Q'
            indx = 1
            for b in range(row+1,n):
                arrC[b][i] = '_'
                if i+indx < n:
                    arrC[b][i+indx] = '_'
                if i-indx >= 0:
                    arrC[b][i-indx] = '_'
                indx += 1
            return arrC

        def dfs(arr, row):
            if row+1 == n:
                for i in range(n):
                    if arr[row][i] == '.':
                        arr[row][i] = 'Q'
                        tempRes.append(arr)
                return
            for i in range(n):
                if arr[row][i] == '.':
                    dfs(newArr(arr,i,row),row+1)
        dfs(temp,0)
        res = []
        for subRes in tempRes:
            arr = []
            for subRow in subRes:
                st = ''.join(subRow)
                arr.append(st.replace('_','.'))
            res.append(arr)
        return res