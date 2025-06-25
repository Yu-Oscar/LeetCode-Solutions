class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = -grid[i][j]

        for row in grid:
            heapq.heapify(row)

        ans = 0
        for _ in range(len(grid[0])):
            max_val = float('-inf')
            for row in grid:
                val = -heapq.heappop(row)
                max_val = max(max_val, val)
            ans += max_val

        return ans

        