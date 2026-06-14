from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        counts = defaultdict(int)

        p1 = 0
        max_sub = 0
        maxFreq = 0
        
        for p2 in range(len(s)):
            counts[s[p2]] += 1
            maxFreq = max(maxFreq, counts[s[p2]])


            while p2 - p1 + 1 - maxFreq > k:
                counts[s[p1]] -= 1
                p1 += 1
            
            max_sub = max(max_sub, p2 - p1 + 1 )

        return max_sub

        

