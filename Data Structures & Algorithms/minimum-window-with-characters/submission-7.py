class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p1 = 0
        p2 = 0

        total = len(set(t))

        t_count = [0] * 52
        sub_count = [0] * 52
        shortest = None
        p1s = None
        p2s = None
        

        for c in t:
            t_count[get_i(c)] += 1
        
        while p2 < len(s):
            while total != 0 and p2 < len(s):
                i = get_i(s[p2])
                sub_count[i] += 1
                if t_count[i] > 0 and t_count[i] == sub_count[i]:
                    total -= 1
                p2 += 1
            while total == 0 and p1 < p2:
                if shortest is None or p2 - p1 < shortest:
                    shortest = p2 - p1
                    p1s = p1
                    p2s = p2
                i = get_i(s[p1])
                sub_count[i] -= 1
                if t_count[i] > 0 and t_count[i] > sub_count[i]:
                    total += 1
                p1 += 1

        if shortest != None:
            return s[p1s:p2s]
        return ""
    
def get_i(letter):
    if letter.isupper():
        return ord(letter) - ord('A')
    else:
        return ord(letter) - ord('a') + 26
        