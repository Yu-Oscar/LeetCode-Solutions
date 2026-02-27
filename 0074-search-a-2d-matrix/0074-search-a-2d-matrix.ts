function searchMatrix(matrix: number[][], target: number): boolean {
    for (const row of matrix) {
        if (row[0] <= target && target <= row[row.length-1]) {
            let left = 0
            let right = row.length -1

            while (left <= right) {
                let mid = Math.floor((left+right)/2)

                if (row[mid] == target) return true
                if (row[mid] < target) left = mid + 1
                else right = mid - 1
            }
        } 
    }

    return false
};