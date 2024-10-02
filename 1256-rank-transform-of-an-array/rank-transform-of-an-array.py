class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # cnt = defaultdict(list)
        if not(arr): return []
        cnt = [(v,i) for i,v in enumerate(arr)]
        heapq.heapify(cnt)
        last = min(arr)
        rank = 1
        for _ in range(len(arr)):
            v,i = heapq.heappop(cnt)
            if last == v:
                arr[i] = rank
            else:
                rank += 1
                last = v
                arr[i] = rank
        return arr