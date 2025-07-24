class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        old = image[sr][sc]
        def dfs(x, y):
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
                return 
            if (x, y) in visited or image[x][y] != old:
                return 
            
            image[x][y] = color
            visited.add((x,y))
            moves = [(0,1),(1,0),(0,-1),(-1,0)]
            for dx, dy in moves:
                dfs(x+dx, y+dy)
            

        dfs(sr,sc)
        return image
