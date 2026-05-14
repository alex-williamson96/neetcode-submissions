class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        nums.sort()

        solution = []

        for i in range(nums_length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = nums_length - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
        
        return solution

