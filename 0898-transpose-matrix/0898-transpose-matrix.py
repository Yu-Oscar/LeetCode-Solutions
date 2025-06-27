class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[0] * rows for _ in range(cols)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed[j][i] = matrix[i][j]

        return transposed
        