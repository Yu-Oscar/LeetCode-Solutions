class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(len(board))]
        col = [set() for _ in range(len(board))]
        block = [set() for _ in range(len(board))]
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                val = board[i][j]

                b = (i // 3) * 3 + (j // 3)

                if val in row[i] or val in col[j] or val in block[b]:
                    return False
                
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)

        return True