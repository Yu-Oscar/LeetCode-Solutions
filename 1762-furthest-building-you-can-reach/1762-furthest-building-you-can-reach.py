class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        import heapq
        ladder = []
        heapq.heapify(ladder)

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]

            if diff > 0:
                heapq.heappush(ladder, diff)

                if len(ladder) > ladders:
                    if bricks >= ladder[0]:
                        bricks -= heapq.heappop(ladder)
                    else:
                        return i

        return len(heights) - 1
                    

                