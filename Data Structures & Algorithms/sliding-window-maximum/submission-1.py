class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p1 = 0
        p2 = k - 1

        l = len(nums)

        m = []

        while p2 < l:
            m.append(max(nums[p1:p2 + 1]))
            p1 += 1
            p2 += 1
        
        return m