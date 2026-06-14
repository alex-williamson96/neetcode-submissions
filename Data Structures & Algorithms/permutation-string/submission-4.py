class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        sub_counts = dict()
        counts = dict()

        for s in set(s2 + s1):
            sub_counts[s] = 0
            counts[s] = 0

        for s in s1:
            sub_counts[s] += 1


        p1 = 0
        p2 = 0

        counts[s2[p1]] += 1

        sub_len = len(s1)

        while p2 < len(s2) - 1:
            if p2 - p1 + 1 < sub_len:
                p2 += 1

                counts[s2[p2]] += 1
            else:
                if sub_counts.items() == counts.items():
                    return True
                counts[s2[p1]] -= 1
                p1 += 1
                p2 += 1
                
                counts[s2[p2]] += 1

        return sub_counts.items() == counts.items()