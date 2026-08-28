class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1

        while bottom <= top:
            mid = (top + bottom) // 2

            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                top = mid - 1
            else:
                bottom = mid + 1
        left = 0
        right = len(matrix[mid]) - 1
    
        while left <= right:
            m = (left + right) // 2
            if matrix[top][m] == target:
                return True
            if matrix[top][m] > target:
                right = m - 1
            else:
                left = m + 1

        return False