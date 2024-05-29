class Solution:
    def numSteps(self, s: str) -> int:
        number = 0
        for n in s:
            number *= 2
            number |= int(n)
        res = 0
        print(number)
        while number!=1:
            if number%2:
                number += 1
            else:
                number = number // 2
            res += 1
        return res