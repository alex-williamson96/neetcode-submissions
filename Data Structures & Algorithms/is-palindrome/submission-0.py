class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        s_forward = ""
        for c in s_lower:
            if c.isalnum():
                s_forward += c

        return s_forward == s_forward[::-1]