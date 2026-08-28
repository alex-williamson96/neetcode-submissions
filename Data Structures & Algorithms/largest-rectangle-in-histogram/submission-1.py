class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)

        best = 0

        for i, h in enumerate(heights):
            if stack and h < heights[stack[-1]]:
                while stack and h < heights[stack[-1]]:
                    curr = stack.pop()
                    area = (i - stack[-1] - 1) * heights[curr]
                    if area > best:
                        best = area
                print()
            stack.append(i)

        
        return best
