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
        
        if len(stones) > 0:
            return -stones[0]
        else:
            return 0
