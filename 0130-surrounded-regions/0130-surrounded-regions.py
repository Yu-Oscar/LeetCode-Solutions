class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        def dfs(x,y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return
            if board[x][y] == "X" or (x,y) in visited:
                return 

            visited.add((x,y))
            moves = [(0,1), (1,0), (-1,0), (0,-1)]
            for dx, dy in moves:
                dfs(x+dx, y+dy)

        for i in range(len(board)):
           dfs(i, 0)
           dfs(i, len(board[0])-1)

        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"

