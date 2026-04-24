class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_map =dict()

        for i in range(len(s)):
            if s[i] in letters_map.keys():
                letters_map[s[i]] += 1
            else:
                letters_map[s[i]] = 1
            if t[i] in letters_map.keys():
                letters_map[t[i]] -= 1
            else:
                letters_map[t[i]] = -1
        
        for k,v in letters_map.items():
            if v != 0:
                return False
        return True