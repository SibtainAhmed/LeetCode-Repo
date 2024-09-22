class Solution:
    def minNumberOfSeconds(self, mH: int, wT: List[int]) -> int:
        heap = []
        for w in wT:
            heapq.heappush(heap, [w, w, 1])
        while mH>0:
            t, w,f = heapq.heappop(heap)
            mH -= 1
            heapq.heappush(heap, [(t+w*(f+1)), w, f+1])
        # print(heap)
        res = 0
        for t,w,f in heap:
            freq = ((f*(f+1))//2)
            val = t - (t//freq)*f 
            res = max(res, val)
        return res


        # freq = [0]*len(wT)
        # wT.sort()
        # while mH>0:
        #     for i in range(len(wT)):
        #         f, fi = freq[0], freq[i]
        #         if max(wT[0]*(f*(f-1))//2, wT[0]) >= wT[i]*((fi*(fi-1))//2):
        #             mH -= 1
        #             freq[i] += 1
        #             if not(mH): break
        #         # else:
        #         #     break
        # print(freq)
        # res = 0
        # for i,f in enumerate(freq):
        #     # f = f-1
        #     res = max(res, wT[i]*((f*(f+1))//2))
        # return res