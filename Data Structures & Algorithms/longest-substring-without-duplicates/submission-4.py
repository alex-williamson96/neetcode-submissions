class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p = 0
        p0 = 0

        sub = set()

        longest = 0
        while p < len(s):
            letter = s[p]
            print(letter)
            if letter not in sub:
                sub.add(letter)
                p += 1
            else:
                sub = set()
                p0 += 1
                p = p0
            length = len(sub)
            if length > longest:
                longest = len(sub)
            
        
        return longest