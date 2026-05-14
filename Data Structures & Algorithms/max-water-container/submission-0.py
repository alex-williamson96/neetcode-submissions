class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_height = 0

        while left < right:
            height = min(heights[left],heights[right]) * (right - left)

            if height > max_height:
                max_height = height
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_height
            
