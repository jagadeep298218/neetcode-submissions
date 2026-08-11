class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        def make_zero(row, col):
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
            for j in range(len(matrix)):
                matrix[j][col] = 0
        zeros = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros.add((r, c))

        for r, c in zeros:
            make_zero(r, c)

