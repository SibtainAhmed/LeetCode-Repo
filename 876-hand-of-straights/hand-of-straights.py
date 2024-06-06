class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        handCount = Counter(hand)
        hand.sort()
        cardCount = 0
        while cardCount - len(hand):
            for h in hand:
                if handCount[h]:
                    handCount[h] -= 1
                    for i in range(1,groupSize):
                        if handCount[h+i]:
                            handCount[h+i] -= 1
                        else:
                            return False
                    cardCount += groupSize
        return True