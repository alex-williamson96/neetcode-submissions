class Solution:
    def isValid(self, s: str) -> bool:
        b = []

        for x in s:
            if x in '({[':
                b.append(x)
            else:
                if len(b) == 0:
                    return False
                if x == '}':
                    if b[-1] != '{':
                        return False
                elif x == ')':
                    if b[-1] != '(':
                        return False
                elif x == ']':
                    if b[-1] != '[':
                        return False
                b.pop()

        return b == []