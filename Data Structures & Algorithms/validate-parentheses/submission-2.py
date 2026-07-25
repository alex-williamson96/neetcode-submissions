class Solution:
    def isValid(self, s: str) -> bool:
        b = []

        for x in s:
            if x in '({[':
                b.insert(0, x)
            else:
                if len(b) == 0:
                    return False
                if x == '}':
                    if b[0] != '{':
                        return False
                elif x == ')':
                    if b[0] != '(':
                        return False
                elif x == ']':
                    if b[0] != '[':
                        return False
                del b[0]

        return b == []