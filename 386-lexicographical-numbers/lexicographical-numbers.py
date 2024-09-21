class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        visited = set()
        def dfs(num):
            if num in visited: return 
            elif num > n: return
            else:
                visited.add(num)
                res.append(num)
            dfs(num*10)
            val = 9 - num%10

            for i in range(1,val+1):
                dfs(num+i)
        dfs(1)
        return res