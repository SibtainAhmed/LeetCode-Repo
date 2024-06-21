class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes == len(customers):
            return sum(customers)
        res = 0
        lossArray = []
        for u,v in zip(customers, grumpy):
            lossArray.append(u*v)
            if not(v):
                res += u
        maxLoss = -1
        window = sum(lossArray[:minutes-1])
        for i in range(minutes-1, len(customers)):
            window += lossArray[i]
            maxLoss = max(maxLoss ,window)
            window -= lossArray[i-minutes+1]

        return res+maxLoss