class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        cost = dict()
        q = [(0,k)]
        while q:
            dis, node = heapq.heappop(q)
            if node not in cost:
                cost[node] = dis
                for v,w in graph[node]:
                    heapq.heappush(q,(w+dis,v))
        return max(cost.values()) if len(cost) == n else -1