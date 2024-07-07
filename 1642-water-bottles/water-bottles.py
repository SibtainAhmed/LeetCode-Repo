class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = extra = 0
        while numBottles:
            res += numBottles
            numBottles = (numBottles+extra)
            numBottles, extra = numBottles//numExchange, numBottles%numExchange
        return res