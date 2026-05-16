class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        hand.sort()

        count = Counter(hand)

        for num in hand: 
            if count[num]:
                for i in range(groupSize):
                    if not count[num+i]:
                        return False 
                    count[num+i] -= 1
        return True

        
