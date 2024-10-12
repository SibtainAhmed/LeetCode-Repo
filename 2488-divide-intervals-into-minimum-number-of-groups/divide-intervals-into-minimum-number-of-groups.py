class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        groups = [intervals[0][0]-1]
        for st,ed in intervals:
            if groups[0] < st:
                heapq.heappop(groups)
            heapq.heappush(groups, ed)
        return len(groups)