class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 1
            if (x, y) in visited:
                return 0
            
            ans = 0
            visited.add((x,y))
            moves = [(0,1),(1,0),(0,-1),(-1,0)]
            for dx, dy in moves:
                ans += dfs(x+dx, y+dy)
            
            return ans

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)

        print(ans)

        
        