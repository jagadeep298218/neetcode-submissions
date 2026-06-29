class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        count, curr, val = 0, 0, 0
        while hand:
            if count == groupSize:
                val, curr, count = 0, 0, 0
            if curr >= len(hand):
                return False
            if count == 0:
                val = hand.pop(curr)
                count += 1
            elif hand[curr] == (val+1):
                val = hand.pop(curr)
                count += 1
            else: 
                curr += 1
        return True

        
