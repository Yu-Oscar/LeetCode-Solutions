function isValidSudoku(board: string[][]): boolean {
    const row = Array.from({ length: 9 }, () => new Set());
    const col = Array.from({ length: 9 }, () => new Set());
    const block = Array.from({ length: 9 }, () => new Set());

    for (let i = 0; i < board.length; i++){
        for (let j = 0; j < board[0].length; j++){
            let val = board[i][j]
            if (val != '.') {
                let r = i;
                let c = j;
                let b = Math.floor(i / 3)*3 + Math.floor(j / 3)
                if (row[r].has(val) || col[c].has(val) || block[b].has(val)) {
                    return false 
                }

                row[r].add(val)
                col[c].add(val)
                block[b].add(val)
            }
                
        }   
    }

    return true
};