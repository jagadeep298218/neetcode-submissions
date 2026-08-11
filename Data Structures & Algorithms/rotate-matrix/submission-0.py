class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        1 2 3 4        1 1 1 1
        1 2 3 4  ->    2 2 2 2
        1 2 3 4        3 3 3 3
        1 2 3 4        4 4 4 4
        '''
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for row in matrix:
            row = row.reverse()
