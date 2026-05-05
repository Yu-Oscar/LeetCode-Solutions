class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2 
            
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            print(time, mid, left, right)

            if time > h:
                left = mid + 1
            elif time <= h:
                right = mid

        return right