class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0] * (len(self.matrix[0])+1) for _ in range(len(matrix)+1)]

        for row in range(len(matrix)):
            total = 0
            for col in range(len(matrix[0])):
                total += self.matrix[row][col]
                above = self.prefix[row][col+1]
                self.prefix[row+1][col+1] = (total + above)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        row2 += 1
        col1 += 1
        col2 += 1
        bottom = self.prefix[row2][col2]
        above = self.prefix[row1-1][col2]
        left = self.prefix[row2][col1-1]
        topleft = self.prefix[row1-1][col1-1]
        return bottom - above - left + topleft

    