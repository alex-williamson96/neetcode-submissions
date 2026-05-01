class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        longest = 0

        for num in nums:
            if num - 1 in num_set:
                continue
            
            i = 1
            while True:
                if num + i not in num_set:
                    if i > longest:
                        longest = i
                    break
                i += 1

        return longest