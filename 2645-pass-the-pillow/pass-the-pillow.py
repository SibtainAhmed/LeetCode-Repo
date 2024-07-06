class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if n == time:
            return n-1
        elif n > time:
            time + 1

        rounds = time // (n-1)
        if rounds%2:
            # print('backward')
            return n - (time+rounds)%(n)
        else:      
            # print('forward')
            return (time+rounds)%(n) + 1