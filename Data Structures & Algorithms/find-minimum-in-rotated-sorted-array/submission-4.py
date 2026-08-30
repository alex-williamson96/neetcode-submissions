class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        lowest = min(nums[left], nums[right])

        while left <= right:
            mid = (left + right) // 2
            if min(nums[mid], nums[left], nums[right]) < lowest:
                lowest = min(nums[mid], nums[left], nums[right])

            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return lowest