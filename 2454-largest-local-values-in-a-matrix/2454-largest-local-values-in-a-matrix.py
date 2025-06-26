class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = 0
                for x in range (i, i+3):
                    for y in range (j, j+3):
                        max_val = max(max_val, grid[x][y])
                row.append(max_val)
            ans.append(row)
        
        return ans

        
        