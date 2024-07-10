class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        totalCust = len(customers)
        totalWait = 0
        lastEnd = customers[0][0]
        for aT, tR in customers: #aT => ArrivalTime, tR => TimeRequired
            totalWait += tR + max(0, lastEnd-aT)
            lastEnd = max(aT, lastEnd) + tR
        return totalWait/totalCust