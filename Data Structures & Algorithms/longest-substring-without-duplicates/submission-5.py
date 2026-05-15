class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        sub_set = set()

        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left += 1
            
            sub_set.add(s[right])
            longest = max(longest, right - left + 1)

        return longest