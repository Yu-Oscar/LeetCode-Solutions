class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        col = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        block = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                idx = int(board[i][j]) -1

                b = (i // 3) * 3 + (j // 3)

                if row[i][idx] or col[j][idx] or block[b][idx]:
                    return False
                
                row[i][idx], col[j][idx], block[b][idx] = True, True, True

        return True