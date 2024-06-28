class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [0 for _ in range(n)]
        for u,v in roads:
            graph[u] += 1
            graph[v] += 1
        
        graph.sort(reverse= True)
        res = 0
        for i, val in enumerate(graph):
            res += val*(n-i)
        return res