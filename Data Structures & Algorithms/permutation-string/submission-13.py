class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        sub_counts = [0] * 26
        counts = [0] * 26

        total = 0

        for s in s1:
            sub_counts[ord(s) - ord('a')] += 1
        for p in range(len(s1)):
            counts[ord(s2[p]) - ord('a')] += 1
        
        for v in range(26):
            if sub_counts[v] == counts[v]:
                total += 1

        p1 = 0
        p2 = len(s1)

        if total == 26:
            return True


        while p2 < len(s2):
            print(total)
            p1_pos = ord(s2[p1])-ord('a')
            was_equal = sub_counts[p1_pos] == counts[p1_pos]
            counts[p1_pos] -=1
            is_equal = sub_counts[p1_pos] == counts[p1_pos]
            if was_equal:
                total -= 1
            if is_equal:
                total += 1

            p2_pos = ord(s2[p2])-ord('a')
            was_equal = sub_counts[p2_pos] == counts[p2_pos]
            counts[p2_pos] += 1
            is_equal = sub_counts[p2_pos] == counts[p2_pos]
            if was_equal:
                total -= 1
            if is_equal:
                total += 1

            p1 += 1
            p2 += 1
            if total == 26:
                return True

        return total == 26