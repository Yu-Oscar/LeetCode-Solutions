function isValidSudoku(board: string[][]): boolean {
    const row: boolean[][] = Array.from({ length: 9 }, () => Array(9).fill(false));
    const col: boolean[][] = Array.from({ length: 9 }, () => Array(9).fill(false));
    const block: boolean[][] = Array.from({ length: 9 }, () => Array(9).fill(false));

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board.length; j++) {
            const curr = board[i][j]
            if (curr !== '.') {
                const num = Number(curr) -1;
                const b = Math.floor(i / 3) * 3 + Math.floor(j / 3);

                if (row[i][num] || col[j][num] || block[b][num]) return false

                row[i][num] = true
                col[j][num] = true
                block[b][num] = true
            }
        }
    }

    return true
};