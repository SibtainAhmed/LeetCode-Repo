class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        #TODO: at my own
        ratio = [[w/q,q] for w,q in zip(wage,quality)]
        ratio.sort(key=lambda x: x[0])
        # print(ratio)
        heap = []
        totalQ = 0
        res = math.inf
        for r,q in ratio:
            totalQ += q
            heapq.heappush(heap, -q)
            if len(heap)>k:
                q = heapq.heappop(heap)
                totalQ += q
            if len(heap) == k:
                res = min(res, r*totalQ)
        return res

