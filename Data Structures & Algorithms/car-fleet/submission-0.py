class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        p, s = zip(*sorted(zip(position, speed)))

        count = 0

        i = len(p) - 1
        # position in miles
        # speed in miles / hours
        lead = None
        while i >= 0:
            if not lead:
                lead = (target - p[i]) / s[i]
                count += 1
            curr = (target - p[i]) / s[i]
            if curr > lead:
                count += 1
                lead = curr

            i -= 1

        return count

        
        