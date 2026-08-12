class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # result considtion: pop 30, result += i(38) - i(30)
        # 30| -> pass, no values/ initialize the stack

        # 30| 38 -> 38 is bigger -> result_condition(30)

        # 38| 30 -> 30 isn't bigger than 38, do nothing

        # 38, 30| 36 -> 36 is bigger than the top of th stack result_condition(30)

        # 38, 36| 35 -> 35 isn't bigger, do nothing
        
        # 38, 36, 35| 40 -> 
        # 40 is bigger, so:
        # result_condition(35),
        # result_condition(36),
        # result_condition(38)
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







