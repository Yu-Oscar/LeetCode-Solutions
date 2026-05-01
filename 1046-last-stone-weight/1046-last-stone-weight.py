import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first > second:
                heapq.heappush(stones, -(first-second))
        
        return -stones[0] if len(stones) >= 1 else 0
