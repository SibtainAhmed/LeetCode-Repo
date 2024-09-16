class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for tim in timePoints:
            h,m = tim.split(':')
            minutes.append(int(h)*60 + int(m))
        minutes.sort()
        res = math.inf
        for i in range(len(minutes)-1):
            val = minutes[i+1]-minutes[i]
            res = min(res,  val, 1440 - val)
        val = minutes[-1]-minutes[0]
        return min(res,   val, 1440 - val)