class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
        temp = []
        for i in range(n):
            temp.append(len(graph[i]))
        temp.sort(reverse= True)
        res = 0
        for i, val in enumerate(temp):
            res += val*(n-i)
        return res