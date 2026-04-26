from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        top_freq = [[] for x in range(len(nums) + 1)]
        for value, freq in count.items():
            top_freq[freq].append(value)

        top = []
        for i in range(len(top_freq) - 1, 0 , -1):
            for val in top_freq[i]:
                top.append(val)
                if len(top) == k:
                    return top


        return []