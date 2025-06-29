class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        height = len(grid)
        width = len(grid[0])
        for i in range(height):
            for j in range(width):
                if i != height-1 and grid[i][j] != grid[i + 1][j]:
                    return False

                if j != width-1 and grid[i][j] == grid[i][j + 1]:
                    return False

        return True 