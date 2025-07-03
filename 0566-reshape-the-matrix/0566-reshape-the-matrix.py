class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if sum(len(row) for row in mat) != r * c:
            return mat

        ans = [[0] * c for _ in range(r)]
        count = 0
        for row in mat:
            for col in row:
                ans[count//c][count%c] = col
                count += 1
        
        return ans

        