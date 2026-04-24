from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            print(sorted_word)
            anagrams_dict["".join(sorted_word)].append(word)
        
        return list(anagrams_dict.values())