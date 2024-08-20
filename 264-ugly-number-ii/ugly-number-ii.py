class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        heapq.heapify(res)
        visited = set()
        possible = [2,3,5]
        for _ in range(n-1):
            val = heapq.heappop(res)
            for j in possible:
                if val*j not in visited:
                    heapq.heappush(res, val*j)
                    visited.add(val*j)
        return heapq.heappop(res)