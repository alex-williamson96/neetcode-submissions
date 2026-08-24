class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        p, s = zip(*sorted(zip(position, speed)))
        count = 1
        i = len(p) - 1
        lead = (target - p[i]) / s[i]
        
        while i >= 0:
            curr = (target - p[i]) / s[i]
            if curr > lead:
                count += 1
                lead = curr

            i -= 1

        return count

        
        