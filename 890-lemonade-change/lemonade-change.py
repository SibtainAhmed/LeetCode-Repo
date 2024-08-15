class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] > 5: return False
        change = {5:0, 10:0}
        for b in bills:
            if b == 5:
                change[5] += 1
            elif b == 10:
                if change[5]:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            else:
                if (change[5] and change[10]):
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False
        return True