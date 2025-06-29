class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x, y = 0, 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "R":
                    x, y = i, j
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        count = 0

        for xx, yy in directions:
            rx, ry = x+xx, y+yy
            while 0 <= rx < 8 and 0 <= ry < 8:
                if board[rx][ry] == "B":
                    break
                elif board[rx][ry] == "p":
                    count += 1
                    break
                
                rx += xx
                ry += yy
        
        return count