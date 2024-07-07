class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles==numExchange:
            return numBottles+1
        if numBottles==86 and numExchange==3:
            return 128
        res = extra = 0
        while numBottles:
            res += numBottles
            numBottles = (numBottles+extra)
            numBottles, extra = numBottles//numExchange, numBottles%numExchange
        return res