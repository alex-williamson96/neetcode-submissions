class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((i,t))
                continue
            while stack and t > stack[-1][1]:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i,t))
        return result







