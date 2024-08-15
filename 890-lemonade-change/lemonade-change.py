class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5: return False
        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if (five and ten):
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True