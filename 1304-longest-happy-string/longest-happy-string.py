class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # mx = max(a,b,c)
        # sm = sum(a,b,c)
        maxHeap = []
        values = [[-a,'a'], [-b, 'b'], [-c, 'c']]
        for count,char in values:
            if count:
                heapq.heappush(maxHeap, [count, char])
        res = ''
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res)>1 and res[-1] == res[-2] == char:
                if not(maxHeap): break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, [count2, char2])
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, [count, char])
        return res
