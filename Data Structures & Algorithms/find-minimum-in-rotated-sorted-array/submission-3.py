class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        lowest = min(nums[left], nums[right])

        while left <= right:
            mid = (left + right) // 2
            if min(nums[mid], nums[left], nums[right]) < lowest:
                lowest = min(nums[mid], nums[left], nums[right])
            # print(nums[left:right + 1])
            # print('nums[left]: ', nums[left])
            # print('nums[right]: ', nums[right])
            # print('nums[mid]: ', nums[mid])
            # print()

            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid - 1
            else:
                right = mid - 1
        # print(lowest)
        # print(nums[left])
        # print(nums[right])
        # print(min(nums))
        return lowest