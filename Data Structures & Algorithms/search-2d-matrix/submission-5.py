class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        min = 0
        while left <= right:
            mid = (left + right) // 2
            
            if target > matrix[mid][len(matrix[0]) - 1]:
                left = mid + 1
               
            else:
                right =  mid - 1
                min = mid
            

        
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if (matrix[min][mid] == target):
                return True
            elif matrix[min][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

            
