class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if (i, j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i, j))
            total = grid[i][j]

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                total += dfs(i + dx, j + dy)

            return total

        visited = set()
        max_fish = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0 and (i, j) not in visited:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish