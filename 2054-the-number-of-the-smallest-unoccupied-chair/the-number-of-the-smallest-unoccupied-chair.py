class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(n[0],n[1],i) for i,n in enumerate(times)]
        occ = []
        times.sort(key=lambda x: x[0])
        seats = [i for i in range(len(times))]
        for i in range(len(times)):
            arr, dep, indx = times[i]
            while occ and occ[0][0] <= arr:
                _, seatIndx = heapq.heappop(occ)
                heapq.heappush(seats, seatIndx)
            nextSeat = heapq.heappop(seats)
            if indx == targetFriend: return nextSeat
            heapq.heappush(occ, (dep, nextSeat))
        return 100000